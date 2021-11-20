from src.model.entity.post import Post
from src.model.entity.tag import Tag
from src.model.entity.user import User
from src.dao.user_dao import UserDao
from src.model.entity.posts_tags import  posts_tags_association_table
from src.model.entity.db_data import Base

if __name__ == '__main__':
    # Base.metadata.create_all()
    # user = User("TestUser4", "1234")
    user_dao = UserDao()
    active_users_list = user_dao.get_all_active_users()
    print("active_users_list:", active_users_list)
    user_by_id = user_dao.get_user_by_id(1)
    print("user_by_id:", user_by_id)

    # get_user_by_id
    # delete_user
    # get_user_by_login
    # get_all_deleted_users