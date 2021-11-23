from typing import Optional
from sqlalchemy.exc import IntegrityError

from src.model.entity.tag import Tag
from src.model.entity.db_data import Session
from src.services.validator_service import validate_input
from src.services.logger_service import main_logger
from src.services.exception_handler_decorator import exception_handler


class TagDao:
    def __init__(self):
        self.__session = Session()

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def save_tag(self, tag: Tag) -> bool:
        validate_input(tag, Tag, "tag")
        self.__session.add(tag)
        self.__session.commit()

        main_logger.info(f"Tag with id:{str(tag.id)} was saved")
        self.__session.close()
        return True

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def update_tag(self, tag: Tag) -> bool:
        validate_input(tag, Tag, "tag")
        self.__session.add(tag)
        self.__session.commit()

        main_logger.info(f"Tag with id:{str(tag.id)} was updated")
        self.__session.close()
        return True

    @exception_handler(exception=IntegrityError,
                       return_value_if_exception=False)
    def delete_tag(self, tag: Tag) -> bool:
        validate_input(tag, Tag, "tag")
        self.__session.query(Tag).filter(Tag.id == tag.id).update({'is_deleted': True})
        self.__session.commit()

        main_logger.info(f"User with id:{str(tag.id)} was deleted")
        self.__session.close()
        return True

    def get_tag_by_name(self, name: str) -> Optional[Tag]:
        validate_input(name, str, "name")
        user = self.__session.query(Tag).filter(Tag.name == name).first()

        main_logger.info(f"Queried tag by name:{name}")
        self.__session.close()

        return user

    def get_tag_by_id(self, tag_id: int) -> Optional[Tag]:
        validate_input(tag_id, int, "id")
        user = self.__session.query(Tag).filter(Tag.id == tag_id).first()

        main_logger.info(f"Queried tag by id:{str(tag_id)}")
        return user

    def get_all_active_tags(self):
        deleted_tags_list = (self.__session.query(Tag)
                             .filter(Tag.is_deleted == False)
                             .all())

        main_logger.info("Queried all active tags")
        self.__session.close()

        return deleted_tags_list

    def get_all_deleted_tags(self):
        deleted_tags_list = (self.__session.query(Tag)
                             .filter(Tag.is_deleted == True)
                             .all())

        main_logger.info("Queried all deleted tags")
        self.__session.close()

        return deleted_tags_list
