# TODO: Feature 2
import pytest
from app import app, movie_repository



def test_display_create_movie_form(test_app):
    """Test if the create movie form is displayed correctly."""
    response = test_app.get("/movies/new")
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
   
    assert b"Create Movie Rating" in response.data

def test_submit_create_movie_form(test_app):


    """Test submitting the create movie form."""
    endClear = movie_repository.clear_db()
    endClear = movie_repository.get_all_movies()
    #checking number of movies
    initial_movies_count = len(endClear)
    
    # Simulating a form submission
    response = test_app.post('/movies', data={
        'title': 'Avengers',
        'director': 'Test Director',
        'rating': 5
    })

    #redirect to movie page
    assert response.status_code == 302
    
    endClear = movie_repository.get_all_movies()
    #checking cout increase
    final_movies_count = len(endClear)
    assert final_movies_count == initial_movies_count + 1

    response = test_app.get("/movies")
    data = response.data.decode('utf-8')
    
    assert response.status_code == 200
    assert "Avengers" in data

    assert "Ironman" not in data
    
    response = test_app.post('/movies', data={
        'title': 'Thor',
        'director': 'Chris',
        'rating': 5
    })
    
    response = test_app.get("/movies")
    data = response.data.decode('utf-8')
    assert "Thor" in data