from locust import HttpUser, task
import requests
import random


def create_id():
    list_id = []
    n = random.randint(1, 10)         # количество объектов, на которых будем замерять скорость
    body = {"data": {"color": "blue", "size": "small"}, "name": "Yulia's Object"}
    for i in range(n):
        response = requests.post('http://167.172.172.115:52353/object', json=body).json()
        list_id.append(response['id'])    # создаем список с id объектов, которые точно будут существовать
    return list_id


class ApiUser(HttpUser):
    obj_id = create_id()

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(3)
    def get_one_object(self):
        self.client.get(f'/object/{random.choice(self.obj_id)}')
