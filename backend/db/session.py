from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings


# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print("Database URL:", SQLALCHEMY_DATABASE_URL)

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

#connecting to sqlite database

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})  # only for SQLite


SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=engine)