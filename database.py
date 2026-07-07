
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "mssql+pyodbc://@LAPTOP-6IN8QLCK/CRUD?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
