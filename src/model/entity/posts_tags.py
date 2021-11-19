from db_data import Base
from sqlalchemy import Column, ForeignKey


class PostsTags(Base):
    __table__ = "posts_tags"

    post_id = Column(ForeignKey("posts.id"), primary_key=True)
    tag_id = Column(ForeignKey("tags.id"), primary_key=True)
