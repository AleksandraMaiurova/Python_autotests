"""
Common fixture
"""
import json
import pytest
import requests

@pytest.fixture(scope="session")
def auth():
    """
    Get token
    """
    response_token = requests.post('https://k-ampus.dev/api/v1/login', json={
        "username": "skhalipa@gmail.com",
        "password": "skhalipa@gmail.com"
    }, timeout=5)
    return json.loads(response_token.text).get('accessToken')
