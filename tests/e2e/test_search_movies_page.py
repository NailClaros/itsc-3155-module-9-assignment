# TODO: Feature 3
import sys
sys.path.append('C:\\Users\\adamn\\OneDrive\\Documents\\GitHub\\itsc-3155-module-9-assignment')
import unittest
from app import app, movie_repository


class TestSearchMoviesPage(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        
        movie_repository.create_movie("Test Movie", "Test Director", 5)

    def test_search_movies_page_loads(self):
        response = self.client.get('/movies/search')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Search Movie Ratings', response.data)

    def test_search_existing_movie(self):
        response = self.client.get('/movies/search?movie_title=Test Movie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Movie', response.data)
        
    def test_search_non_existing_movie(self):
        response = self.client.get('/movies/search?movie_title=Random Movie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'No movie found with the provided title.', response.data)

if __name__ == "__main__":
    unittest.main()
