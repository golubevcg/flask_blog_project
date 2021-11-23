from src.model.entity.post import Post
from src.model.entity.user import User
from src.dao.user_dao import UserDao
from src.dao.tag_dao import TagDao
from src.dao.post_dao import PostDao


if __name__ == '__main__':

    user_dao = UserDao()

    user = User("trala1la", "1234")
    print(user_dao.save_user(user))

    # POST DAO TESTS
    post_dao = PostDao()
    tag_dao = TagDao()
    user_dao = UserDao()
    active_tags = tag_dao.get_all_active_tags()

    print("active_tags:", active_tags)
    user_by_id = user_dao.get_user_by_id(30)

    print("user_by_id:", user_by_id)
    post = Post("header5", "body", list(active_tags), user_by_id)

    print(post)
    post_dao.save_post(post)

    print(post)
