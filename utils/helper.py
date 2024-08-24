import allure
import json
from allure_commons.types import AttachmentType


class Helper:
    @allure.step("Attach response")
    def attach_response(self, response):
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    def assert_response_status_code(self, response, status_code):
        with allure.step(f"Check response status code is {status_code}"):
            assert response.status_code == status_code, response.status_code
