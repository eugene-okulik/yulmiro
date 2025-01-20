import pytest
from test_api_ymironova.endpoints.post_object import PostObject
from test_api_ymironova.endpoints.delete_object import DeleteObject
from test_api_ymironova.endpoints.get_object import GetObject
from test_api_ymironova.endpoints.put_object import PutObject
from test_api_ymironova.endpoints.patch_object import PatchObject


@pytest.fixture
def create_post_obj():
    return PostObject()


@pytest.fixture
def create_delete_obj():
    return DeleteObject()


@pytest.fixture
def create_get_obj():
    return GetObject()


@pytest.fixture
def create_put_obj():
    return PutObject()


@pytest.fixture
def create_patch_obj():
    return PatchObject()


@pytest.fixture
def setup_and_teardown():
    data = {"data": {"color": "green", "size": "large"},"name": "Yulia's Object"}
    obj_for_test = PostObject()
    response = obj_for_test.create_obj(data)
    obj_id = response.json()['id']
    yield obj_id
    obj_for_delete = DeleteObject()
    obj_for_delete.delete_obj(obj_id)


@pytest.fixture
def setup():
    data = {"data": {"color": "green", "size": "large"},"name": "Yulia's Object"}
    obj_for_test = PostObject()
    response = obj_for_test.create_obj(data)
    obj_id = response.json()['id']
    return obj_id


@pytest.fixture(scope="session")
def start_finish_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture
def switch_test():
    print('before test')
    yield
    print('after test')
