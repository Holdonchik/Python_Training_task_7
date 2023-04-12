import requests
import pytest
from Open_brewery_API import *

URL = "https://api.openbrewerydb.org/v1/breweries"


class TestOpenBrewery:
    def test_get_single_brewery(self):
        response = requests.request("GET", f"{URL}/b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0")
        Assertions.assert_code_status(response, 200)
        Assertions.validate_schema(response, brewery_schema)

    def test_list_breweries(self):
        response = requests.request("GET", URL)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_schemas(response, brewery_schema)

    @pytest.mark.parametrize("city", ["San Diego","Austin", "Norman"])
    def test_list_breweries_by_city(self, city):
        params = {"city": city}
        response = requests.request("GET", URL, params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_schemas(response, brewery_schema)
        Assertions.assert_key_values(response, "city", city, "equal")

    @pytest.mark.parametrize("name", ["brewerie", "coop", "beer"])
    def test_list_breweries_by_name(self, name):
        params = {"name": name}
        response = requests.request("GET", URL, params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_schemas(response, brewery_schema)
        Assertions.assert_key_values(response, "name", name, "contains")

    @pytest.mark.parametrize(["name", "city"],
                             [("brewerie", "San Diego"),
                              ("coop", "Austin"),
                              ("beer", "Norman")
                              ])
    def test_list_breweries_by_name_and_city(self, name, city):
        params = {"name": name}
        response = requests.request("GET", URL, params=params)
        Assertions.assert_code_status(response, 200)
        Assertions.validate_schemas(response, brewery_schema)
        Assertions.assert_key_values(response, "name", name, "contains")
        Assertions.assert_key_values(response, "city", city, "equal")