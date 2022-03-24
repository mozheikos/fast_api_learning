from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession as Session
# from sqlalchemy.ext.asyncio import create_async_engine as create_engine

from core.config import DATABASE_URL

database = Database(DATABASE_URL)

metadata = MetaData()
engine = create_engine(DATABASE_URL,)
# session = Session(bind=engine)
Base = declarative_base()
