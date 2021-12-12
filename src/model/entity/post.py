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

    def __init__(self,
                 header: str,
                 body: str,
                 is_published: bool = False,
                 is_link_access: bool = False,
                 is_deleted: bool = False):
        validate_input(header, str, "header")
        validate_input(body, str, "body")

        header_length = len(header)
        if header_length < 5 or header_length > 50:
            raise Exception("Header length does not fit between 5 and 50 symbols, saving interrupted!")

        self.header = header
        self.body = body

        now = datetime.now()
        self.creation_date = now.strftime("%d/%m/%Y %H:%M:%S")

        self.is_published = is_published
        self.is_link_access = is_link_access
        self.is_deleted = is_deleted

    def __str__(self):
        return f"Post(id:{self.id})"

    def to_dict(self):
        return {"header": self.header,
                "body": self.body,
                "id": str(self.id),
                "is_deleted": self.is_deleted,
                "is_published": self.is_published,
                "creation_date": self.creation_date.strftime("%d %b"),
                "is_link_access": self.is_link_access}
