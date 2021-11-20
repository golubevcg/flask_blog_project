from src.model.entity.post import Post
from src.model.entity.db_data import Session
from src.model.entity.tag import Tag
from src.model.entity.user import User
from src.services.logger_service import main_logger
from src.services.validator_service import validate_input
from typing import Optional


class PostDao:
    def __init__(self):
        self.__session = Session

    def _open_close_session(func):
        def inner(self, *args):
            self.__session = self.__session()
            result = func(self, *args)
            self.__session.close()
            return result

        return inner

    @_open_close_session
    def save_post(self, post: Post) -> bool:
        validate_input(post, Post, "post")
        self.__session.add(post)
        self.__session.commit()
        main_logger.info(f"Post with id:{str(post.id)} has been saved")
        return True

    @_open_close_session
    def update_post(self, post: Post) -> bool:
        validate_input(post, Post, "post")
        self.__session.add(post)
        self.__session.commit()
        main_logger.info(f"Post with id:{str(post.id)} has been updated")
        return True

    @_open_close_session
    def delete_post(self, post: Post) -> bool:
        validate_input(post, Post, "post")
        post.is_deleted = True
        post_id = post.id
        self.__session.commit()
        self.__session.add(post)
        main_logger.info(f"Post with id:{str(post_id)} has been deleted")
        return True

    @_open_close_session
    def get_all_active_posts(self) -> list:
        active_posts_list = self.__session.query(Post).filter(Post.is_deleted == False)
        self.__session.commit()
        main_logger.info("Querying all active posts")
        return active_posts_list

    @_open_close_session
    def get_post_by_id(self, post_id: int) -> Optional[Post]:
        validate_input(post_id, int, "post_id")
        post = self.__session.query(Post).filter_by(id=post_id).one_or_none()
        main_logger.info(f"Querying post with id:{str(post_id)}")
        return post

    @_open_close_session
    def get_post_with_header_like(self, header: str) -> list:
        validate_input(header, str, "header")
        posts_list = self.__session.query(Post).filter(Post.header.ilike(header))
        main_logger.info(f"Querying posts with header ilike:{header}")
        return posts_list

    @_open_close_session
    def get_posts_by_tag_id(self, tag_id: int) -> list:
        validate_input(tag_id, int, "tag_id")
        posts = (self.__session
                 .query(Post)
                 .join(Post.tags)
                 .filter(Tag.id == tag_id)
                 .all
                 )
        main_logger.info(f"Querying posts by tag_id:{str(tag_id)}")
        return posts

    @_open_close_session
    def get_posts_by_tag_name(self, tag_name: str) -> list:
        validate_input(tag_name, str, "tag_name")
        posts = (self.__session
                 .query(Post)
                 .join(Post.tags)
                 .filter(Tag.name == tag_name)
                 .all
                 )
        main_logger.info(f"Querying posts by tag_name:{tag_name}")
        return posts

    @_open_close_session
    def get_posts_by_author_id(self, author_id: int) -> list:
        validate_input(author_id, int, "author_id")
        posts = (self.__session
                 .query(Post)
                 .join(Post.author)
                 .filter(User.id == author_id)
                 .all
                 )
        main_logger.info(f"Querying posts by author_id:{str(author_id)}")
        return posts

    @_open_close_session
    def get_posts_by_author_login(self, login: str) -> list:
        validate_input(login, str, "login")
        posts = (self.__session
                 .query(Post)
                 .join(Post.author)
                 .filter(User.login == login)
                 .all
                 )
        main_logger.info(f"Querying posts by login:{login}")
        return posts

    @_open_close_session
    def get_deleted_posts(self) -> list:
        deleted_posts_list = self.__session.query(Post).filter(Post.is_deleted == True)
        self.__session.commit()
        main_logger.info("Querying all deleted posts")
        return deleted_posts_list
