from sqlalchemy import (Column, DateTime, ForeignKey, Integer, MetaData,
                        String, Table, func)

metadata = MetaData()

login_table = Table(
    "login",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("created_at", DateTime, default=func.now()),
)
plan_table = Table(
    "plan",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("max_profiles", Integer, nullable=False),
    Column("login_id", Integer, ForeignKey("login.id"), unique=True, nullable=False),
)
profile_table = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), nullable=False),
    Column("icon", String(255)),
    Column("login_id", Integer, ForeignKey("login.id"), nullable=False),
    Column("create_at", DateTime, default=func.now()),
    Column("update_at", DateTime, default=func.now(), onupdate=func.now()),
)
