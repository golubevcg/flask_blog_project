from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from model.entity.post import Post
from services.logger_service import main_logger
from services.validator_service import validate_input
from services.warning_handler_decorator import exception_handler
from services.db_service import db


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def save_post(post: Post) -> bool:
    header_length = len(post.header)
    if header_length < 5 or header_length > 50:
        main_logger.warning("Header length does not fit between 5 and 50 symbols, saving interrupted!")
        return ""

    validate_input(post, Post, "post")
    db.session.add(post)
    db.session.commit()

    main_logger.info(f"Post with id:{str(post.id)} has been saved")
    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def delete_post(post: Post) -> bool:
    validate_input(post, Post, "post")
    delete_post_by_id(post.id)

    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def delete_post_by_id(post_id):
    if not post_id:
        return False
    Post.query.filter_by(id=post_id).update({'is_deleted': True})
    db.session.commit()
    main_logger.info(f"Post with id {post_id} marked as deleted.")


def get_all_active_posts() -> list:
    active_posts_list = (Post.query
                         .filter(Post.is_deleted == False)
                         .order_by(desc(Post.creation_date))
                         .all())

    main_logger.info("Querying all active posts")
    return active_posts_list


def get_all_published_posts() -> list:
    active_posts_list = (Post.query
                         .filter(Post.is_deleted == False)
                         .filter(Post.is_published == True)
                         .filter(Post.is_link_access == False)
                         .order_by(desc(Post.creation_date))
                         .all()
                         )

    main_logger.info("Querying published posts")

    return active_posts_list


def get_all_posts_from_page(page_num: int) -> list:
    all_posts_list = (Post.query
                      .order_by(desc(Post.creation_date))
                      .paginate(page=page_num, per_page=10)
                      .items
                      )
    main_logger.info("Querying all posts on page: %s" % str(page_num))
    return all_posts_list


def get_all_published_posts_from_page(page_num: int) -> list:
    active_posts_list = (Post.query
                         .filter(Post.is_deleted == False)
                         .filter(Post.is_published == True)
                         .filter(Post.is_link_access == False)
                         .order_by(desc(Post.creation_date))
                         .paginate(page=page_num, per_page=10)
                         .items
                         )

    main_logger.info("Querying published posts on page: %s" % str(page_num))
    return active_posts_list


def get_posts_amount():
    posts_amount = (Post.query
                    .filter(Post.is_deleted == False)
                    .filter(Post.is_published == True)
                    .filter(Post.is_link_access == False)
                    .count())

    main_logger.info("Querying posts amount.")

    return posts_amount


def get_all_published_through_link_posts() -> list:
    active_posts_list = (Post.query
                         .filter(Post.is_deleted == False)
                         .filter(Post.is_published == True)
                         .filter(Post.is_link_access == True)
                         .order_by(desc(Post.creation_date))
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
                  .order_by(desc(Post.creation_date))
                  .all())

    main_logger.info(f"Querying posts with header ilike:{header}")
    return posts_list


def get_post_with_by_header(header: str) -> list:
    validate_input(header, str, "header")
    posts_list = (Post.query
                  .filter(Post.header == header)
                  .order_by(desc(Post.creation_date))
                  .all())

    main_logger.info(f"Querying posts with header ilike:{header}")
    return posts_list


def get_deleted_posts() -> list:
    deleted_posts_list = (Post.query
                          .order_by(desc(Post.creation_date))
                          .filter(Post.is_deleted == True))

    main_logger.info("Querying all deleted posts")
    return deleted_posts_list


def commit():
    db.session.commit()
