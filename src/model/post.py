from db_data import Base
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from user import User
from datetime import datetime


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False)
    body = Column(String, nullable=False)
    author = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts_list")

    tags = relationship("Tag", back_populates="Tag")

    def __init__(self, header: str, body: str, tags: list, author: User):
        self.header = header
        self.body = body
        self.tags = tags
        self.author = author
        now = datetime.now()
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_deleted = False
