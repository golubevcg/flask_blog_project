from .db_data import Base
from sqlalchemy import Table, Column, ForeignKey


posts_tags_association_table = Table('posts_tags', Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True)
)
