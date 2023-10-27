# TODO: Feature 2
import pytest
from app import app,  movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

def test_create_movie_empty(test_app):
    response = test_app.get('/movies')
    data = response.data.decode('utf-8')

    Repo = movie_repository.clear_db()
    assert Repo is None
    Repo = movie_repository.get_all_movies()
    assert "Avengers" not in Repo


def test_create_movies_page(test_app):

    movie = movie_repository.create_movie("Avengers", "Anthony", 2)
    target = movie_repository.get_movie_by_title("Avengers")
    Repo = movie_repository.get_all_movies()
    assert movie.title == target.title
    assert Repo is not None



    
    