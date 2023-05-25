from requests import Response
import json
import re


class Assertions:
    @staticmethod
    def assert_status_text(response: Response):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert response_as_dict["status"] == "success", f"Incorrect status {response_as_dict['status']}." \
                                                        f"Expected status: 'success'"

    @staticmethod
    def assert_json_has_keys_message_and_status(response: Response):
        names = ["message", "status"]
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for name in names:
            assert name in response_as_dict, f"Response JSON doesn't have key '{name}'"

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_image_pattern(response: Response, name, expected_pattern):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert re.search(expected_pattern, response_as_dict[name]), F"Message does not match the pattern"

    @staticmethod
    def assert_images_pattern(response: Response, images, expected_pattern):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        for image in response_as_dict[images]:
            assert re.search(expected_pattern, image), F"Image {image} does not match the pattern"