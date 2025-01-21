import requests
import allure
from test_api_ymironova.endpoints.endpoint import Endpoint


class GetObject(Endpoint):

    @allure.step('Show object')
    def get_obj(self, obj_id):
        self.response = requests.get(f'{self.url}/{obj_id}')
        self.json = self.response.json()
        return self.response

    @allure.step('Check that id is correct')
    def check_response_id_is_correct(self, obj_id):
        assert self.json['id'] == obj_id
