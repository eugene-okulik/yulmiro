import allure

class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    json = None

    @allure.step('Check that response code is correct')
    def check_response_code_is_correct(self):
        assert self.response.status_code == 200