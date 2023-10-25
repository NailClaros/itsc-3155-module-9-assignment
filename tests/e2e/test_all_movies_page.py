from app import movie_repository
def test_all_movies_empty(test_app):
    respone = test_app.get('/movies')
    data = respone.data.decode('utf-8')
    movie_repository.clear_db()

    assert respone.status_code == 200
    assert '</li>' in data

def test_all_movies_with_2_movies(test_app):
    movie_repository.create_movie('Bionicle 1', 'Steve Goldenburg', 1)
    movie_repository.create_movie('Johnathan Wickman', 'Stanford Rubix', 5)
    respone = test_app.get('/movies')
    data = respone.data.decode('utf-8')

    assert 'Bionicle 1' in data
    assert 'Steve Goldenburg' in data

    assert 'Johnathan Wickman' in data
    assert 'Stanford Rubix' in data

    assert len(movie_repository.get_all_movies()) == 2

    assert 'ROBOMAN 5' not in data
    assert 'Marvin Scorch' not in data

def test_all_movies_removal(test_app):
    xid = 0
    for id, mov in movie_repository.get_all_movies().items():
        if mov.title == 'Bionicle 1':
            xid = id
    movie_repository.delete_movie(xid)

    respone = test_app.get('/movies')
    data = respone.data.decode('utf-8')

    assert len(movie_repository.get_all_movies()) == 1
    assert 'Bionicle 1' not in data
    assert 'Steve Goldenburg' not in data

    assert 'Johnathan Wickman' in data
    assert 'Stanford Rubix' in data

def test_all_movies_not_in_rep(test_app):
    respone = test_app.get('/movies')
    data = respone.data.decode('utf-8')

    assert 'THIS MOVIE IS NOT IN REP' not in data
    assert 'fake director' not in data
