import pytest
from app import routes

def test_home_page(test_client):
    '''
    Given a Flask application
    When the '/' page is requested
    Then check if the response is valid
    '''
    response = test_client.get('/')
    assert response.status_code == 200