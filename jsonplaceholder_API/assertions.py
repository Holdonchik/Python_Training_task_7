from requests import Response
import json
import re


class Assertions:
    @staticmethod
    def assert_key_value(response: Response, name, expected_value, action):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        if action == "equal":
            assert response_as_dict[name] == expected_value, f"Incorrect key value {response_as_dict[name]}." \
                                                             f"Expected value: {expected_value}"
        elif action == "not equal":
            assert response_as_dict[name] != expected_value, f"Values are equal. But expected to be not equal"

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
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

