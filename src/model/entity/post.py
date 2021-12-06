from sqlalchemy import (
    Column, String, Integer,
    Boolean, DateTime,
    func, Text)
from datetime import datetime
from src.services.validator_service import validate_input
from services.db_service import db


class Post(db.Model):
    __tablename__ = "posts"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    header = Column(String, nullable=False, unique=True)
    body = Column(Text, nullable=False)
    creation_date = Column(DateTime, nullable=False, server_default=func.now())
    is_published = Column(Boolean, nullable=False, default=False)
    is_link_access = Column(Boolean, nullable=False, default=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    def __init__(self, header: str, body: str, is_published: bool = False, is_link_access: bool = False):
        validate_input(header, str, "header")
        validate_input(body, str, "body")

        self.header = header
        self.body = body

        now = datetime.now()
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_deleted = False
        if is_published:
            self.is_published = is_published

        if is_link_access:
            self.is_link_access = is_link_access

    def __str__(self):
        return f"Post(id:{self.id})"
