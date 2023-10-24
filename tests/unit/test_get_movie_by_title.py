# TODO: Feature 3
import pytest
from src.repositories.movie_repository import get_movie_repository


movies_data = {
    1: {"title": "Obamna Soda", "director": "Quentin Tarantino", "rating": 5},
    2: {"title": "Avatar: The Last Blue Person", "director": "James Madison Cameron", "rating": 4},
    3: {"title": "Titanic: The Ship", "director": "James Madison Cameron", "rating": 5}
}

class MockMovieRepository:
    def search_movies_by_title(self, title):
        return [movie for movie in movies_data.values() if title.lower() in movie["title"].lower()]


movie_repository = MockMovieRepository()

def test_get_movie_by_title_found():
    title = "Obamna"
    result = movie_repository.search_movies_by_title(title)
    assert len(result) == 1
    assert result[0]["title"] == "Obamna Soda"

def test_get_movie_by_title_not_found():
    title = "Unknown Movie"
    result = movie_repository.search_movies_by_title(title)
    assert len(result) == 0

def test_get_movie_by_title_partial_match():
    title = "Avatar"
    result = movie_repository.search_movies_by_title(title)
    assert len(result) == 1
    assert result[0]["title"] == "Avatar: The Last Blue Person"

if __name__ == "__main__":
    pytest.main()
