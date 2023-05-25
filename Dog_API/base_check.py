from requests import Response
from Dog_API.assertions import Assertions


class BaseCheck:
    @staticmethod
    def base_check_success_case(response: Response):
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_keys_message_and_status(response)
        Assertions.assert_status_text(response)
