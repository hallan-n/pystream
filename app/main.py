import uvicorn
from fastapi import FastAPI
from infra.routes.login import login

app = FastAPI()

app.include_router(login)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
