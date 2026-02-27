from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class JobModel(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    salary = Column(Integer)
    is_remote = Column(Boolean, default=False)