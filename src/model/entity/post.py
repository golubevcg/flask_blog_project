from .user import User
from sqlalchemy import (
    Column, String, Integer,
    ForeignKey, Boolean, DateTime,
    func, Text)
from sqlalchemy.orm import relationship
from datetime import datetime
from src.services.validator_service import validate_input
from .db_data import db


class Post(db.Model):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False, unique=True)
    body = Column(Text, nullable=False)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)

    author_id = Column(Integer,
                       ForeignKey(User.id),
                       nullable=False,
                       unique=False)
    author = relationship("User", back_populates="posts_list", lazy='joined')

    def __init__(self, header: str, body: str, author: User):
        validate_input(header, str, "header")
        validate_input(body, str, "body")
        validate_input(author, User, "author")

        self.header = header
        self.body = body
        self.author = author

        now = datetime.now()
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_deleted = False

    def __str__(self):
        return f"Pots(id:{self.id})"
