import requests
import allure
from test_api_ymironova.endpoints.endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step('Delete object')
    def delete_obj(self, obj_id):
        self.response = requests.delete(f'{self.url}/{obj_id}')
        return self.response
