from typing import Optional
from sqlalchemy.exc import IntegrityError

from src.model.entity.post import Post
from src.services.logger_service import main_logger
from src.services.validator_service import validate_input
from src.services.exception_handler_decorator import exception_handler
from services.db_service import db


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def save_post(post: Post) -> bool:
    validate_input(post, Post, "post")
    db.session.add(post)
    db.session.commit()

    main_logger.info(f"Post with id:{str(post.id)} has been saved")
    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def delete_post(post: Post) -> bool:
    validate_input(post, Post, "post")
    post_id = post.id
    delete_post_by_id(post.id)

    main_logger.info(f"Post with id:{str(post_id)} has been deleted")
    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def delete_post_by_id(post_id):
    if not post_id:
        return False
    Post.query.filter_by(id=post_id).update({'is_deleted': True})
    db.session.commit()


def get_all_active_posts() -> list:
    active_posts_list = (Post.query
                         .filter(Post.is_deleted == False)
                         .all())
    main_logger.info("Querying all active posts")

    return active_posts_list


def get_post_by_id(post_id: int) -> Optional[Post]:
    validate_input(post_id, int, "post_id")
    post = Post.query.filter(Post.id == post_id).first()

    main_logger.info(f"Querying post with id:{str(post_id)}")
    return post


def get_post_with_header_like(header: str) -> list:
    validate_input(header, str, "header")
    posts_list = (Post.query
                  .filter(Post.header.ilike(header))
                  .all())

    main_logger.info(f"Querying posts with header ilike:{header}")
    return posts_list


def get_post_with_by_header(header: str) -> list:
    validate_input(header, str, "header")
    posts_list = (Post.query
                  .filter(Post.header == header)
                  .all())

    main_logger.info(f"Querying posts with header ilike:{header}")
    return posts_list


def get_deleted_posts() -> list:
    deleted_posts_list = (Post.query
                          .filter(Post.is_deleted == True))

    main_logger.info("Querying all deleted posts")
    return deleted_posts_list


def commit():
    db.session.commit()
