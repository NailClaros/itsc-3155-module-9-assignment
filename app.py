from flask import Flask, redirect, render_template, url_for, abort, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()
movie_repository.create_movie("Obamna Soda", "Quentin Tarantino", 5)
movie_repository.create_movie("Avatar: The Last Blue Person", "James Madison Cameron", 4)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/movies')
def list_all_movies():
    return render_template('list_all_movies.html', movie_repository=movie_repository.get_all_movies())

@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)

@app.post('/movies')
def create_movie():
    title = request.form.get('title')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))
    movie_repository.create_movie(title, director, rating) 
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search', methods=['GET'])
def search_movies():
    # TODO: Feature 3
    title = request.args.get('movie_title')
    
    if not title:
        return render_template('search_movies.html')
    
    all_movies = movie_repository.get_all_movies()
    matched_movie = next((movie for movie in all_movies.values() if title.lower() in movie.title.lower()), None)



@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = get_movie_repository().get_movie_by_id(movie_id)

    if(movie_id not in movie_repository.get_all_movies().keys()):
        abort(404)
    else:
        return render_template('get_single_movie.html', movie=movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass
