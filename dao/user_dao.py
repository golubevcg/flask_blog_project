from typing import Optional
from sqlalchemy.exc import IntegrityError

from model.entity.user import User
from services.validator_service import validate_input
from services.logger_service import main_logger
from services.exception_handler_decorator import exception_handler
from services.db_service import db


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def save_user(user: User) -> bool:
    validate_input(user, User, "user")
    db.session.add(user)
    db.session.commit()
    main_logger.info(f"User with id:{str(user.id)} was saved")
    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def update_user(user: User) -> bool:
    validate_input(user, User, "user")
    db.session.add(user)
    db.session.commit()

    main_logger.info(f"User with id:{str(user.id)} was updated")
    return True


@exception_handler(exception=IntegrityError,
                   return_value_if_exception=False)
def delete_user(user: User) -> bool:
    validate_input(user, User, "user")
    (User.query
     .filter(User.id == user.id)
     .update({'is_deleted': True}))
    db.session.commit()

    main_logger.info(f"User with id:{str(user.id)} was deleted")
    return True


def get_user_by_id(user_id: int) -> Optional[User]:
    validate_input(user_id, int, "user_id")
    user = User.query.filter(User.id == user_id).first()

    main_logger.info(f"Queried user by id:{str(user_id)}")
    return user


def get_user_by_login(login: str) -> Optional[User]:
    validate_input(login, str, "login")
    user = (User.query
            .filter(User.login == login)
            .first())

    main_logger.info(f"Queried user by login:{login}")
    return user


def get_all_active_users() -> list:
    active_users_list = (User.query
                         .filter(User.is_deleted == False)
                         .all())

    main_logger.info("Queried all active users")
    return active_users_list


def get_all_deleted_users() -> list:
    deleted_users_list = (User.query
                          .filter(User.is_deleted == True)
                          .all())

    main_logger.info("Queried all deleted users")
    return deleted_users_list

def commit():
    db.session.commit()