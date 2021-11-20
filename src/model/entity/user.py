from .db_data import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from datetime import datetime
from sqlalchemy.orm import relationship
import hashlib
from src.services.validator_service import validate_input


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    registration_date = Column(DateTime, nullable=False, server_default=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)
    posts_list = relationship("Post", back_populates="user")

    def __init__(self, login: str, password: str):
        validate_input(login, str, "login")
        validate_input(password, str, "password")

        self.login = login
        password = str(password).encode()
        self.password = hashlib.md5(password).hexdigest()
        now = datetime.now()
        self.registration_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_deleted = False