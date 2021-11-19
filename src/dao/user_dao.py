from src.model.entity.user import User
from src.model.entity.db_data import Session
from src.services.exception_handler_decorator import exception_handler
from src.services.validator_service import validate_input
from src.services.logger_service import main_logger
from typing import Optional


class UserDao:
    def __init__(self):
        self.__session = Session

    @exception_handler(False)
    def save_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__session.save(user)
        main_logger.info(f"User with id:{str(user.id)} has been saved")
        return True

    @exception_handler(False)
    def update_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__session.save(user)
        main_logger.info(f"User with id:{str(user.id)} has been updated")
        return True

    @exception_handler(False)
    def delete_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        user.is_deleted = True
        self.__session.save(user)
        main_logger.info(f"User with id:{str(user.id)} has been deleted")
        return True

    @exception_handler(None)
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        validate_input(user_id, int, "user_id")
        user = self.__session.query(User).filter_by(id=user_id).one_or_none()
        main_logger.info(f"Querying user with id:{str(user_id)}")
        return user

    @exception_handler(None)
    def get_user_by_login(self, login: str) -> Optional[User]:
        validate_input(login, str, "login")
        user = self.__session.query(User).filter_by(User.login == login).one_or_none()
        main_logger.info(f"Querying user with login:{login}")
        return user

    @exception_handler([])
    def get_all_active_users(self) -> list:
        active_users_list = self.__session.query(User).filter(User.is_deleted == False)
        self.__session.commit()
        main_logger.info("Querying all active users")
        return active_users_list

    @exception_handler([])
    def get_all_deleted_users(self) -> list:
        deleted_users_list = self.__session.query(User).filter(User.is_deleted == True)
        self.__session.commit()
        main_logger.info("Querying all deleted users")
        return deleted_users_list


