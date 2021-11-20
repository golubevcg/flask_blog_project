from .db_data import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from src.services.validator_service import validate_input
from .posts_tags import posts_tags_association_table


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    is_deleted = Column(Boolean, nullable=False, default=False)

    posts = relationship(
        "Post",
        back_populates="tags",
        secondary=posts_tags_association_table,
    )

    def __init__(self, name: str):
        validate_input(name, str, "name")
        self.name = name
