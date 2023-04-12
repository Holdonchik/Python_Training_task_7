import pytest
import requests
from jsonplaceholder_API import *


class TestJsonPlaceHolder:
    @pytest.mark.parametrize(["resource", "expected_number"], [
        ('posts', 100),
        ('comments', 500),
        ('albums', 100),
        ('photos', 5000),
        ('todos', 200),
        ('users', 10)
    ])
    def test_get_resource(self, resource, expected_number):
        response = requests.get(f"https://jsonplaceholder.typicode.com/{resource}")
        response_as_dict = response.json()

        Assertions.assert_code_status(response, 200)
        assert len(response_as_dict) == expected_number

    @pytest.mark.parametrize(["resource", "expected_number"], [
        ('posts', 101),
        ('comments', 501),
        ('albums', 101),
        ('photos', 5001),
        ('todos', 201),
        ('users', 11)
    ])
    def test_create_resource(self, resource, expected_number):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {'title': 'test',
                   'body': 'test body',
                   'userId': 1}
        data = json.dumps(payload, indent=4)

        response = requests.post(f"https://jsonplaceholder.typicode.com/{resource}", headers=headers, data=data)

        Assertions.assert_code_status(response, 201)
        Assertions.assert_key_value(response, 'title', payload['title'], "equal")
        Assertions.assert_key_value(response, 'body', payload['body'], "equal")
        Assertions.assert_key_value(response, 'userId', payload['userId'], "equal")
        Assertions.assert_key_value(response, 'id', expected_number, "equal")

    @pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
    def test_update_resource(self, resource):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {'id': 1,
                   'title': 'updated',
                   'body': 'test body updated',
                   'userId': 1}
        data = json.dumps(payload, indent=4)

        response1 = requests.get(f"https://jsonplaceholder.typicode.com/posts/1")
        response2 = requests.put(f"https://jsonplaceholder.typicode.com/{resource}/1", headers=headers, data=data)
        res_as_dict1 = response1.json()

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_key_value(response2, 'title', payload['title'], "equal")
        Assertions.assert_key_value(response2, 'body', payload['body'], "equal")
        Assertions.assert_key_value(response2, 'body', payload['body'], "equal")
        Assertions.assert_key_value(response2, 'id', 1, "equal")
        Assertions.assert_key_value(response2, "title", res_as_dict1['title'], "not equal")
        Assertions.assert_key_value(response2, "body", res_as_dict1['body'], "not equal")

    @pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
    def test_patch_resource(self, resource):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {'title': 'updated'}
        data = json.dumps(payload, indent=4)

        response1 = requests.get(f"https://jsonplaceholder.typicode.com/posts/1")
        response2 = requests.patch(f"https://jsonplaceholder.typicode.com/{resource}/1", headers=headers, data=data)
        res_as_dict1 = response1.json()

        Assertions.assert_code_status(response2, 200)
        Assertions.assert_key_value(response2, 'title', payload['title'], "equal")
        Assertions.assert_key_value(response2, 'id', 1, "equal")
        Assertions.assert_key_value(response2, "title", res_as_dict1['title'], "not equal")

    @pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
    def test_delete_resource(self, resource):
        headers = {'Content-type': 'application/json; charset=UTF-8'}
        payload = {'userId': 1}
        data = json.dumps(payload, indent=4)

        response = requests.delete(f"https://jsonplaceholder.typicode.com/{resource}/1", headers=headers, data=data)

        Assertions.assert_code_status(response, 200)

    @pytest.mark.parametrize('resource', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
    def test_return_all_related_to_user(self, resource):
        payload = {'userId': 1}
        data = json.dumps(payload, indent=4)

        response = requests.get(f"https://jsonplaceholder.typicode.com/{resource}", params=data)

        Assertions.assert_code_status(response, 200)

    @pytest.mark.parametrize(["resource", "sub_recourse", "keys"], [
        ('posts', 'comments', ["postId", "id", "name", "email", "body"]),
        ('albums', 'photos', ["albumId", "id", "title", "url", "thumbnailUrl"]),
        ('users', 'albums', ["userId", "id", "title"]),
        ('users', 'todos', ["userId", "id", "title", "completed"]),
        ('users', 'posts', ["userId", "id", "title", "body"])
    ])
    def test_return_all_sub_resource_related_to_user(self, resource, sub_recourse, keys):
        response = requests.get(f'https://jsonplaceholder.typicode.com/{resource}/1/{sub_recourse}')
        response_as_dict = response.json()

        Assertions.assert_code_status(response, 200)

        index = range(0, len(response_as_dict) - 1)
        for val in index:
            for key in keys:
                assert key in response_as_dict[val], f"Response JSON doesn't have key '{key}'"

