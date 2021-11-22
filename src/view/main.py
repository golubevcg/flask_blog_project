from src.model.entity.post import Post
from src.model.entity.tag import Tag
from src.model.entity.user import User
from src.dao.user_dao import UserDao
from src.dao.tag_dao import TagDao

from src.dao.post_dao import PostDao

from src.model.entity.posts_tags import  posts_tags_association_table
from src.model.entity.db_data import Base


if __name__ == '__main__':






    # POST DAO TESTS
    post_dao = PostDao()
    active_tags = tag_dao.get_all_active_tags()
    print("active_tags:", active_tags)
    user_by_id = user_dao.get_user_by_id(30)
    print("user_by_id:", user_by_id)
    post = Post("header", "body", list(active_tags), user_by_id)
    print(post)
    post_dao.save_post(post)
    print(post)

