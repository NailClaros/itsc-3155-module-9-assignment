# TODO: Feature 4
import pytest
from flask.testing import FlaskClient
from app import app, get_single_movie
from src.repositories.movie_repository import get_movie_repository



@pytest.fixture()
def test_app() -> FlaskClient:
    return app.test_client()

get_movie_repository().clear_db()
star_wars = get_movie_repository().create_movie("Star Wars", "George Lucas", 5)
dune = get_movie_repository().create_movie("Dune", "No Idea", 3)
avatar = get_movie_repository().create_movie("Avatar", "James Cameron", 100)

def test_movie_not_found(test_app: FlaskClient) -> None:
    response = test_app.get('/movies/12345')

    assert response.status_code == 404


def test_get_star_wars(test_app: FlaskClient) -> None:

    response = test_app.get(f'/movies/{star_wars.movie_id}')
    data = response.data.decode()
    
    assert response.status_code == 200
    assert 'Star Wars' in data



def test_get_dune(test_app: FlaskClient) -> None:

    response = test_app.get(f'/movies/{dune.movie_id}')
    data = response.data.decode()
        
    assert response.status_code == 200
    assert 'Dune' in data

def test_get_avatar(test_app: FlaskClient) -> None:

    response = test_app.get(f'/movies/{avatar.movie_id}')
    data = response.data.decode()
        
    assert response.status_code == 200
    assert '100 Stars!' in data


