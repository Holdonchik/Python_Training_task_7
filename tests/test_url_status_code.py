import requests


def test_status_code_of_url(url, status_code):
    response = requests.get(url=url)
    assert response.status_code == status_code
