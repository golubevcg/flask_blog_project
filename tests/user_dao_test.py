import pytest
from src.model.entity.post import Post
from src.model.entity.tag import Tag
from src.model.entity.user import User
from src.dao.user_dao import UserDao


@pytest.fixture()
def user_dao_fixture():
    return UserDao()


def test_get_active_users_list(user_dao_fixture):
    active_users_list = user_dao_fixture.get_all_active_users()
    assert len(active_users_list) == 3


def test_get_user_by_id(user_dao_fixture):
    user_by_id = user_dao_fixture.get_user_by_id(29)
    assert user_by_id.id == 29


def test_get_user_by_login(user_dao_fixture):
    user_by_login = user_dao_fixture.get_user_by_login("TestUser")
    assert user_by_login.login == "TestUser"


def test_get_all_deleted_users(user_dao_fixture):
    all_deleted_users = user_dao_fixture.get_all_deleted_users()
    assert len(all_deleted_users) == 1