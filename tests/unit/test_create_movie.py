# TODO: Feature 2
import pytest
from app import app, movie_repository

@pytest.fixture()
def test_app():
    return app.test_client()

def test_display_create_movie_form(test_app):
    """Test if the create movie form is displayed correctly."""
    response = test_app.get("/movies/new")
    
    assert response.status_code == 200
    # Assuming you have some distinctive phrases in your form, like:
    assert b"Create Movie Rating" in response.data

def test_submit_create_movie_form(test_app):
    """Test submitting the create movie form."""
    
    # Before submission, let's check the current number of movies
    initial_movies_count = len(movie_repository.get_all_movies())
    
    # Simulating a form submission
    response = test_app.post('/movies', data={
        'title': 'Test Movie',
        'director': 'Test Director',
        'rating': 5
    })

    # Expecting a redirect to the movie list page
    assert response.status_code == 302
    assert 'Location' in response.headers
    assert response.headers['Location'].endswith('/movies')
    
    # Check if the movie count increased by 1 after the form submission
    final_movies_count = len(movie_repository.get_all_movies())
    assert final_movies_count == initial_movies_count + 1

    # Optional: Check if the new movie is present in the repository (this would need more repository functions)

# You can add more tests for edge cases, incorrect form inputs, etc.
