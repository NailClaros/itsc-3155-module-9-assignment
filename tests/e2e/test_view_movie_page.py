# TODO: Feature 4
from flask.testing import FlaskClient
from app import movie_repository


def test_movie_not_found(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    star_wars = movie_repository.create_movie("Star Wars", "George Lucas", 5)
    response = test_app.get('/movies/12345')
    data = response.data.decode()

    assert response.status_code == 404
    assert 'Star Wars' not in data


def test_get_star_wars(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    star_wars = movie_repository.create_movie("Star Wars", "George Lucas", 5)

    response = test_app.get(f'/movies/{star_wars.movie_id}')
    data = response.data.decode()

    assert response.status_code == 200
    assert f'{star_wars.title}' in data
    assert f'{star_wars.director}' in data
    assert f'{star_wars.rating}' in data


def test_get_star_wars_with_two_movies(test_app: FlaskClient) -> None:
    movie_repository.clear_db()
    star_wars = movie_repository.create_movie("Star Wars", "George Lucas", 5)
    avatar = movie_repository.create_movie("Avatar", "James Cameron", 5)

    response = test_app.get(f'/movies/{star_wars.movie_id}')
    data = response.data.decode()

    assert response.status_code == 200
    assert f'{avatar.title}' not in data
    assert f'{avatar.director}' not in data
    assert f'{star_wars.title}' in data
    assert f'{star_wars.director}' in data



