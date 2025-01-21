import requests
import allure
from test_api_ymironova.endpoints.endpoint import Endpoint


class PutObject(Endpoint):

    @allure.step('Modification object')
    def put_obj(self, obj_id, data):
        self.response = requests.put(f'{self.url}/{obj_id}', json=data)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that modification is correct')
    def check_response_change_put_is_correct(self, data):
        assert self.json['data']['material'] == data['data']['material']
