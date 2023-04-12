from jsonschema import validate
from requests import Response
import json
import re

class Assertions:
    @staticmethod
    def validate_schema(response: Response, expected_schema):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
        validate(instance=response_as_dict, schema=expected_schema)

    @staticmethod
    def validate_schemas(response: Response, expected_schema):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"
            for val in response_as_dict:
                validate(instance=response_as_dict, schema=expected_schema)
    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}. Actual: {response.status_code}"

    @staticmethod
    def assert_key_values(response: Response, name, expected_value, action):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        for val in response_as_dict:
            if action == "equal":
                assert response_as_dict[name] == expected_value, f"Incorrect key value {response_as_dict[name]}." \
                                                                 f"Expected value: {expected_value}"
            elif action == "contains":
                assert expected_value in response_as_dict[name], f"Incorrect key value {response_as_dict[name]}." \
                                                                 f"Expected to contain: {expected_value}"


