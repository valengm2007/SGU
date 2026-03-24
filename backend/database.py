from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://sgu_user:1s7g67u_@localhost/sgu"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

