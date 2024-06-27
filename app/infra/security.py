from datetime import datetime, timedelta
from os import getenv

import bcrypt
from fastapi import Header, HTTPException, status
from infra.cache import Cache
from jose import JWTError, jwt


class Security:
    @classmethod
    def hashed(self, password: str):
        salt = bcrypt.gensalt()
        hash = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hash.decode("utf-8")

    @classmethod
    def check_hash(self, hashed: str, password: str):
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

    @classmethod
    def create_access_token(self, data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(
                minutes=int(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode, getenv("SECRET_KEY"), algorithm=getenv("ALGORITHM")
        )
        return encoded_jwt

    @classmethod
    def revoke_access_token(self, token: str):
        Cache.set("blacklist", token)

    @classmethod
    def decode_token(self, token: str = Header(...)):
        try:
            payload = jwt.decode(
                token, getenv("SECRET_KEY"), algorithms=getenv("ALGORITHM")
            )
            if Cache.has("blacklist", str(payload)):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token incorreto ou expirado.",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token incorreto ou expirado.",
                headers={"WWW-Authenticate": "Bearer"},
            )
