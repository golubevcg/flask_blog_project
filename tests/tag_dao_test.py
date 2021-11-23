import pytest
from src.dao.tag_dao import TagDao


@pytest.fixture()
def tagdao_fixture():
    return TagDao()


def test_get_all_active_tags(tagdao_fixture):
    all_active_tags = tagdao_fixture.get_all_active_tags()
    assert len(all_active_tags) == 1


def test_get_tag_by_name(tagdao_fixture):
    returned_tag = tagdao_fixture.get_tag_by_name("tag1")
    assert returned_tag.name == "tag1"


def test_get_tag_by_id(tagdao_fixture):
    tag_by_id = tagdao_fixture.get_tag_by_id(10)
    assert tag_by_id.id == 10


def get_all_deleted_tags(tagdao_fixture):
    deleted_tags = tagdao_fixture.get_all_deleted_tags()
    assert len(deleted_tags) == 1
