import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

#from databases import Database
#from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.path.join(BASE_DIR, ".env")

DATABASE_URL="postgresql://postgres:password@jagaad:5432/stats_message"

#SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]


#db = Database(os.environ["DATABASE_URL"])
db = create_engine(DATABASE_URL)
metadata = sqlalchemy.MetaData()


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
