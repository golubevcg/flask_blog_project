from src.model.entity.user import User
from src.model.entity.db_data import Session
from src.services.validator_service import validate_input
from src.services.logger_service import main_logger
from typing import Optional


class UserDao:
    def __init__(self):
        self.__session = Session()

    def _open_close_session(func):
        def inner(self, *args):
            result = func(self, *args)
            return result
        return inner


    @_open_close_session
    def save_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__session.add(user)
        self.__session.commit()
        self.__session.close()

        main_logger.info(f"User with id:{str(user.id)} was saved")
        return True

    @_open_close_session
    def update_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        self.__session.add(user)
        self.__session.commit()
        self.__session.close()

        main_logger.info(f"User with id:{str(user.id)} was updated")
        return True

    @_open_close_session
    def delete_user(self, user: User) -> bool:
        validate_input(user, User, "user")
        user.is_deleted = True
        self.__session.add(user)
        self.__session.commit()
        self.__session.close()

        main_logger.info(f"User with id:{str(user.id)} was deleted")
        return True

    @_open_close_session
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        validate_input(user_id, int, "user_id")
        user = self.__session.query(User).filter(User.id == user_id).one_or_none()
        self.__session.close()

        main_logger.info(f"Queried user with id:{str(user_id)}")
        return user

    @_open_close_session
    def get_user_by_login(self, login: str) -> Optional[User]:
        validate_input(login, str, "login")
        user = self.__session.query(User).filter(User.login == login)
        main_logger.info(f"Queried user with login:{login}")

        self.__session.close()
        return user

    @_open_close_session
    def get_all_active_users(self) -> list:
        active_users_list = self.__session.query(User).all()
        main_logger.info("Queried all active users")

        self.__session.close()
        return active_users_list

    @_open_close_session
    def get_all_deleted_users(self) -> list:
        deleted_users_list = self.__session.query(User).filter(User.is_deleted == True)
        main_logger.info("Queried all deleted users")

        self.__session.close()
        return deleted_users_list
