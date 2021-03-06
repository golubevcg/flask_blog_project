from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from flask_login import UserMixin
from datetime import datetime
import hashlib
from services.validator_service import validate_input
from services.db_service import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    registration_date = Column(DateTime,
                               nullable=False,
                               server_default=func.now())
    is_deleted = Column(Boolean, nullable=False, default=False)

    def __init__(self, login: str, password: str):
        validate_input(login, str, "login")
        validate_input(password, str, "password")

        self.login = login
        password = str(password).encode()
        self.password = hashlib.md5(password).hexdigest()
        now = datetime.now()
        self.registration_date = now.strftime("%d/%m/%Y %H:%M:%S")
        self.is_deleted = False

    def __str__(self):
        return f"{self.login}" \
               f"(id:{str(self.id)}, " \
               f"is_deleted:{str(self.is_deleted)})"
