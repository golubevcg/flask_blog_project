from src.model.entity.post import Post
from src.model.entity.tag import Tag
from src.model.entity.user import User
from src.dao.user_dao import UserDao
from src.model.entity.posts_tags import  posts_tags_association_table
from src.model.entity.db_data import Base

if __name__ == '__main__':
    # Base.metadata.create_all()
    user = User("TestUser", "1234")
    user_dao = UserDao()
    user_dao.save_user(user)
