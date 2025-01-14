import pytest
import requests


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


@pytest.fixture()
def new_obj():
    body = {
        "data": {
            "color": "green",
            "size": "large"
        },
        "name": "Yulia's Object"
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body).json()
    obj_id = response['id']
    yield obj_id
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


@pytest.mark.critical
@pytest.mark.parametrize(
    'title',
    [
        {"data": {"color": "green", "size": "large"}, "name": "Yulia's Object1"},
        {"data": {"color": "yellow", "size": "small"}, "name": "Yulia's Object2"},
        {"data": {"color": "red", "size": "medium"}, "name": "Yulia's Object3"}
    ]
)
def test_create_obj(title, switch_test, start_finish_testing):
    body = title
    response = requests.post('http://167.172.172.115:52353/object', json=body).json()
    assert response["name"] == title["name"]


def test_get_obj(new_obj, switch_test):
    response = requests.get(f'http://167.172.172.115:52353/object/{new_obj}').json()
    assert response['id'] == new_obj


def test_put_obj(new_obj, switch_test):
    body = {
        "data": {
            "color": "green",
            "size": "large",
            "material": "silk"
        },
        "name": "Yulia's Object"
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{new_obj}', json=body).json()
    assert response['data']['material'] == 'silk', 'Error'


def test_patch_obj(new_obj, switch_test):
    body = {
        "data": {
            "color": "orange",
            "size": "small",
            "material": "silk"
        }
    }
    requests.patch(f'http://167.172.172.115:52353/object/{new_obj}', json=body).json()


@pytest.mark.medium
def test_delete_obj(new_obj, switch_test):
    response = requests.delete(f'http://167.172.172.115:52353/object/{new_obj}')
    assert response.status_code == 200, 'Error'
