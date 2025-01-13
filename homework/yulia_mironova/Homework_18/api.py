import requests


def create_obj():
    body = {
        "data": {
            "color": "blue",
            "size": "small"
        },
        "name": "Yulia's Object"
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body).json()
    obj_id = response['id']
    clear_obj(obj_id)


def new_obj():
    body = {
        "data": {
            "color": "green",
            "size": "large"
        },
        "name": "Yulia's Object"
    }
    response = requests.post('http://167.172.172.115:52353/object', json=body).json()
    return response['id']


def clear_obj(obj_id):
    requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')


def put_obj():
    obj_id = new_obj()
    body = {
        "data": {
            "color": "green",
            "size": "large",
            "material": "silk"
        },
        "name": "Yulia's Object"
    }
    response = requests.put(f'http://167.172.172.115:52353/object/{obj_id}', json=body).json()
    assert response['data'] ['material'] == 'silk', 'Error'
    clear_obj(obj_id)


def patch_obj():
    obj_id = new_obj()
    body = {
        "data": {
            "color": "orange",
            "size": "small",
            "material": "silk"
        }
    }
    response = requests.patch(f'http://167.172.172.115:52353/object/{obj_id}', json=body).json()
    clear_obj(obj_id)


def delete_obj():
    obj_id = new_obj()
    response = requests.delete(f'http://167.172.172.115:52353/object/{obj_id}')
    assert response.status_code == 200, 'Error'


create_obj()
put_obj()
patch_obj()
delete_obj()
