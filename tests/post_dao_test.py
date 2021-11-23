import pytest
from src.dao.post_dao import PostDao


@pytest.fixture()
def postdao_fixture():
    return PostDao()


def test_get_all_active_posts(postdao_fixture):
    result = postdao_fixture.get_all_active_posts()
    assert len(result) == 1


def test_get_post_by_id(postdao_fixture):
    post = postdao_fixture.get_post_by_id(1)
    assert post.id == 1


def test_get_post_with_header_like(postdao_fixture):
    posts = postdao_fixture.get_post_with_header_like("header")
    assert len(posts) == 1
    assert posts[0].id == 1


def test_get_posts_by_tag_id(postdao_fixture):
    posts = postdao_fixture.get_posts_by_tag_id(9)
    assert len(posts) == 1
    assert posts[0].body == "body"


def test_get_posts_by_tag_name(postdao_fixture):
    posts = postdao_fixture.get_posts_by_tag_name("tag2")
    assert len(posts) == 1
    assert posts[0].header == "header"


def test_get_posts_by_author_id(postdao_fixture):
    posts = postdao_fixture.get_posts_by_author_id(30)
    assert len(posts) == 1
    assert posts[0].author.id == 30


def test_get_posts_by_author_login(postdao_fixture):
    pass