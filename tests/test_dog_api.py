import requests
from Dog_API import *
from Dog_API.assertions import Assertions
import pytest


class TestDogAPI(BaseCheck):
    def test_list_by_bread(self):
        response = requests.get(URL+"/breeds/list/all")
        self.base_check_success_case(response)

    @pytest.mark.parametrize('breed', breeds)
    def test_list_by_sub_bread(self, breed):
        response = requests.get(f"{URL}/breed/{breed}/list")
        self.base_check_success_case(response)

    def test_random_image(self):
        response = requests.get(URL + "/breeds/image/random")
        expected_pattern = r"^https://images\.dog\.ceo/breeds/.*\.jpg$"

        self.base_check_success_case(response)
        Assertions.assert_image_pattern(response, "message", expected_pattern)


    @pytest.mark.parametrize('count', [2, 10, 20, 30, 50])
    def test_multiple_random_image(self, count):
        response = requests.get(f"{URL}/breeds/image/random/{count}")
        response_as_dict = response.json()
        expected_pattern = r"^https://images\.dog\.ceo/breeds/.*\.jpg$"

        self.base_check_success_case(response)
        Assertions.assert_images_pattern(response, "message", expected_pattern)
        assert len(response_as_dict["message"]) == count, f"Number of images requested {count}," \
                                                          f" does not match number of images returned" \
                                                          f"{len(response_as_dict['message'])}"

    @pytest.mark.parametrize('breed', breeds)
    def test_random_image_from_subbreed(self, breed):
        response1 = requests.get(f"{URL}/breed/{breed}/list")
        response_as_dict = response1.json()
        sub_breeds = response_as_dict["message"]

        if len(sub_breeds) == 0:
            pass
        else:
            for sub_breed in sub_breeds:
                expected_pattern = fr"^https://images\.dog\.ceo/breeds/{breed}-{sub_breed}.*\.jpg$"
                response2 = requests.get(f"{URL}/breed/{breed}/{sub_breed}/images/random")
                self.base_check_success_case(response2)
                Assertions.assert_image_pattern(response2, "message", expected_pattern)


    @pytest.mark.parametrize('count', [3, 50])
    @pytest.mark.parametrize('breed', breeds)
    def test_multiple_random_image_from_subbreed(self, breed, count):
        response1 = requests.get(f"{URL}/breed/{breed}/list")
        response_as_dict = response1.json()
        sub_breeds = response_as_dict["message"]
        if len(sub_breeds) == 0:
            pass
        else:
            for sub_breed in sub_breeds:
                expected_pattern = fr"^https://images\.dog\.ceo/breeds/{breed}-{sub_breed}.*\.jpg$"
                response2 = requests.get(f"{URL}/breed/{breed}/{sub_breed}/images/random/{count}")
                self.base_check_success_case(response2)
                Assertions.assert_images_pattern(response2, "message", expected_pattern)


    @pytest.mark.parametrize('breed', breeds)
    def test_get_image_by_bread(self, breed):
        response = requests.get(f"{URL}/breed/{breed}/images")

        expected_pattern = fr"^https://images\.dog\.ceo/breeds/{breed}.*\.jpg$"
        self.base_check_success_case(response)
        Assertions.assert_images_pattern(response, "message", expected_pattern)


    @pytest.mark.parametrize('breed', breeds)
    def test_get_random_image_by_bread(self, breed):
        response = requests.get(f"{URL}/breed/{breed}/images/random")

        expected_pattern = fr"^https://images\.dog\.ceo/breeds/{breed}.*\.jpg$"

        self.base_check_success_case(response)
        Assertions.assert_image_pattern(response, "message", expected_pattern)


    @pytest.mark.parametrize('count', [2, 10, 20, 30, 50])
    @pytest.mark.parametrize('breed',  breeds)
    def test_get_more_than_one_image_by_bread(self, breed, count):
        response = requests.get(f"{URL}/breed/{breed}/images/random/{count}")

        expected_pattern = fr"^https://images\.dog\.ceo/breeds/{breed}.*\.jpg$"
        self.base_check_success_case(response)
        Assertions.assert_images_pattern(response, "message", expected_pattern)

