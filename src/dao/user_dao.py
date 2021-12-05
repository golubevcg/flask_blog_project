from typing import Optional
from sqlalchemy.exc import IntegrityError

from src.model.entity.user import User
from src.services.validator_service import validate_input
from src.services.logger_service import main_logger
from src.services.exception_handler_decorator import exception_handler


class UserDao:
    def __init__(self, db):
        self.__db = db

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def save_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__db.session.add(user)
        self.__db.session.commit()
        main_logger.info(f"User with id:{str(user.id)} was saved")
        return True

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def update_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__db.session.add(user)
        self.__db.session.commit()

        main_logger.info(f"User with id:{str(user.id)} was updated")
        return True

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def delete_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        (User.query
         .filter(User.id == user.id)
         .update({'is_deleted': True}))
        self.__db.session.commit()

        main_logger.info(f"User with id:{str(user.id)} was deleted")
        return True

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        validate_input(user_id, int, "user_id")
        user = User.query.filter(User.id == user_id).first()

        main_logger.info(f"Queried user by id:{str(user_id)}")
        User.close()
        return user

    def get_user_by_login(self, login: str) -> Optional[User]:
        validate_input(login, str, "login")
        user = (User.query
                .filter(User.login == login)
                .first())

        main_logger.info(f"Queried user by login:{login}")
        return user

    def get_all_active_users(self) -> list:
        active_users_list = (User.query
                             .filter(User.is_deleted == False)
                             .all())

        main_logger.info("Queried all active users")
        return active_users_list

    def get_all_deleted_users(self) -> list:
        deleted_users_list = (User.query
                              .filter(User.is_deleted == True)
                              .all())

        main_logger.info("Queried all deleted users")
        return deleted_users_list
