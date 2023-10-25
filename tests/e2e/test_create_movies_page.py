# TODO: Feature 2
import pytest
from app import app

@pytest.fixture(scope='module')
def test_client():
    with app.test_client() as client:
        yield client

def test_access_create_movies_page(test_client):
    # Make a GET request to the create movies page
    response = test_client.get('/movies/new')

    # Assert the status code
    assert response.status_code == 200

    # Assert that the response contains the expected text
    assert b"Create Movie Rating" in response.data
