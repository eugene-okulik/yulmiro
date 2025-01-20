import pytest

DATA = [
    {"data": {"color": "green", "size": "large"}, "name": "Yulia's Object1"},
    {"data": {"color": "yellow", "size": "small"}, "name": "Yulia's Object2"},
    {"data": {"color": "red", "size": "medium"}, "name": "Yulia's Object3"}
]

PUT_DATA = [{"data": {"color": "green", "size": "large", "material": "silk"}, "name": "Yulia's Object1"}]

PATCH_DATA = [{"data": {"color": "orange", "size": "large", "material": "silk"}}]


@pytest.mark.parametrize('data', DATA)
def test_create_obj(data, create_post_obj, start_finish_testing, switch_test):
    create_post_obj.create_obj(data)
    create_post_obj.check_response_name_is_correct(data)


def test_delete_obj(switch_test, create_delete_obj, setup):
    create_delete_obj.delete_obj(setup)
    create_delete_obj.check_response_code_is_correct()


def test_get_obj(switch_test, create_get_obj, setup_and_teardown):
    create_get_obj.get_obj(setup_and_teardown)
    create_get_obj.check_response_id_is_correct(setup_and_teardown)


@pytest.mark.parametrize('put_data', PUT_DATA)
def test_put_obj(switch_test, create_put_obj, setup_and_teardown, put_data):
    create_put_obj.put_obj(setup_and_teardown, put_data)
    create_put_obj.check_response_change_put_is_correct()


@pytest.mark.parametrize('patch_data', PATCH_DATA)
def test_patch_obj(switch_test, create_patch_obj, setup_and_teardown, patch_data):
    create_patch_obj.patch_obj(setup_and_teardown, patch_data)
    create_patch_obj.check_response_change_patch_is_correct()
