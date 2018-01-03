import media
import fresh_tomatoes


def list_movies():
    """ Creates the list of movies to display in the web-page"""
    movies = []

    movies.append(media.Movie(
        "Monty Python's Life of Brian",
        "Religious satire comedy",
        "https://vignette1.wikia.nocookie.net/greatest-movies/images/3/3f/Monty_pythons_life_of_brian.jpg/revision/latest?cb=20170820100523",  # NOQA
        "https://www.youtube.com/watch?v=HxIlg4m5fns"))

    movies.append(media.Movie(
        "Monty Python and the Holy Grail",
        "Slapstick comedy concerning the Arthurian legend",
        "http://img.moviepostershop.com/monty-python-and-the-holy-grail-movie-poster-1975-1010465239.jpg",  # NOQA
        "https://www.youtube.com/watch?v=hKNDml12Big"))

    movies.append(media.Movie(
        "Annie Hall",
        "Romantic adventures of two neurotic New Yorkers",
        "http://img.moviepostershop.com/annie-hall-movie-poster-1977-1010725380.jpg",  # NOQA
        "https://www.youtube.com/watch?v=OqVgCfZX-yE"))

    return movies

# Create a list of movies to be displayed on the Website
movies = list_movies()

# Create the HTML file and open it in default webbrowser
fresh_tomatoes.open_movies_page(movies)
