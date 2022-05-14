from sqlalchemy import Integer, String
from sqlalchemy.sql.schema import Column
from .database import Base


class Job(Base):
    __tablename__ = "jobs"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nulltable=False)
    description = Column(String, nulltable=False)
    
# $ alembic init alembic
# go to the alembic.ini file and change the sqlalchemy.url to your database url (postgresql://postgres:[...])
# $ alembic revision -m "init"
# this crates a script inside alembic/versions/, change de upgrade function to create the table and the downgrade function to drop it
# $ alembic upgrade head
# $ touch src/schemas.py
