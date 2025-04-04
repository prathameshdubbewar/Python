from sqlalchemy import Column, Integer, String
from .database import Base  # Ensure this uses a relative import

class Blog(Base):
    __tablename__ = "blogs"  # Define the table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
