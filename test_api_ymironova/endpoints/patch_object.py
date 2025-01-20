import requests
import allure
from test_api_ymironova.endpoints.endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step('Modification object')
    def patch_obj(self, obj_id, data):
        self.response = requests.patch(f'{self.url}/{obj_id}', json=data)
        self.json = self.response.json()
        return self.response

    @allure.step('Check that modification is correct')
    def check_response_change_patch_is_correct(self):
        assert self.json['data']['color'] == 'orange'
