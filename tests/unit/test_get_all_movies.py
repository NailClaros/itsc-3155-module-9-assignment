# TODO: Feature 1
import pytest
from app import app, movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

def test_list_all_movies_empty(test_app):
    response = test_app.get('/movies')

    assert response.status_code == 200
    ##clear and assert the movie list is empty
    M_R = movie_repository.clear_db()
    
    assert M_R is None

def test_list_all_movies_size(test_app):
    response = test_app.get('/movies')

    assert response.status_code == 200
    ##clear and assert the movie list is empty
    M_R = movie_repository.clear_db()
    assert M_R is None

    movie_repository.create_movie("Bionicle 1", "Mr.Jeevez", "1")
    M_R = movie_repository.get_all_movies()
    assert M_R is not None
    assert len(M_R) is 1

    movie_repository.create_movie("Johnathan Wickman", "Michele bay", "3")
    M_R = movie_repository.get_all_movies()
    assert len(M_R) is 2

    M_R.popitem()
    assert len(M_R) is 1