from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table, func

metadata = MetaData()

login_table = Table(
    "login",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(255), nullable=False, unique=True),
    Column("password", String(255), nullable=False),
    Column("created_at", DateTime, default=func.now()),
)
