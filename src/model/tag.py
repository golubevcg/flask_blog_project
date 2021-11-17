from db_data import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    def __init__(self, name: str):
        self.name = name