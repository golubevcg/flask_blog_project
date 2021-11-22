from src.model.entity.user import User
from src.model.entity.db_data import Session
from src.services.validator_service import validate_input
from src.services.logger_service import main_logger
from typing import Optional


class UserDao:
    def __init__(self):
        self.__session = Session()

    def save_user(self, user: User):
        validate_input(user, User, "user")
        self.__session.add(user)
        self.__session.commit()

        main_logger.info(f"User with id:{str(user.id)} was saved")
        self.__session.close()

    def update_user(self, user: User):
        validate_input(user, User, "user")
        self.__session.add(user)
        self.__session.commit()

        main_logger.info(f"User with id:{str(user.id)} was updated")
        self.__session.close()

    def delete_user(self, user: User):
        validate_input(user, User, "user")
        self.__session.query(User).filter(User.id == user.id).update({'is_deleted': True})
        self.__session.commit()

        main_logger.info(f"User with id:{str(user.id)} was deleted")
        self.__session.close()

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        validate_input(user_id, int, "user_id")
        user = self.__session.query(User).filter(User.id == user_id).one_or_none()

        main_logger.info(f"Queried user by id:{str(user_id)}")
        self.__session.close()
        return user

    def get_user_by_login(self, login: str) -> Optional[User]:
        validate_input(login, str, "login")
        user = self.__session.query(User).filter(User.login == login).one_or_none()

        main_logger.info(f"Queried user by login:{login}")
        self.__session.close()
        return user

    def get_all_active_users(self) -> list:
        active_users_list = self.__session.query(User).filter(User.is_deleted == False).all()

        main_logger.info("Queried all active users")
        self.__session.close()
        return active_users_list

    def get_all_deleted_users(self) -> list:
        deleted_users_list = self.__session.query(User).filter(User.is_deleted == True).all()

        main_logger.info("Queried all deleted users")
        self.__session.close()
        return deleted_users_list
