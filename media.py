import webbrowser


class Movie():
    """ This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """Stores the information related to a movie.

        Args:
            movie_title : the title of the movie
            movie_storyline : the storyline of the movie
            poster_image: url of a poster image
            trailer_youtube: url of a youtube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Plays the youtube trailer in the webbrowser."""
        webbrowser.open(self.trailer_youtube_url)
