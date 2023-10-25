# TODO: Feature 4
import pytest
from flask.testing import FlaskClient
from app import app, movie_repository, get_single_movie



@pytest.fixture()
def test_app() -> FlaskClient:
    return app.test_client()


def test_movie_not_found(test_app: FlaskClient) -> None:
    response = test_app.get('/movies/12345')

    assert response.status_code == 404


def test_get_star_wars(test_app: FlaskClient) -> None:
    
    movie_repository.clear_db()
    star_wars = movie_repository.create_movie("Star Wars", "George Lucas", 5)

    response = test_app.get(f'/movies/{star_wars.movie_id}')
    data = response.data.decode()
    
    assert response.status_code == 200
    assert f'{star_wars.title}' in data
    assert f'{star_wars.director}' in data
    assert f'{star_wars.rating} Stars' in data


def test_get_dune(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    dune = movie_repository.create_movie("Dune", "No Idea", 3)

    response = test_app.get(f'/movies/{dune.movie_id}')
    data = response.data.decode()
        
    assert response.status_code == 200
    assert 'Dune' in data

def test_get_avatar(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    avatar = movie_repository.create_movie("Avatar", "James Cameron", 5)

    response = test_app.get(f'/movies/{avatar.movie_id}')
    data = response.data.decode()
        
    assert response.status_code == 200
    assert 'James Cameron' in data
    

