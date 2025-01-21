import requests
import allure
from test_api_ymironova.endpoints.endpoint import Endpoint


class PostObject(Endpoint):

    @allure.step('Create new object')
    def create_obj(self, body):
        self.response = requests.post(f'{self.url}', json=body)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that name is correct')
    def check_response_name_is_correct(self, title):
        assert self.json["name"] == title["name"]
