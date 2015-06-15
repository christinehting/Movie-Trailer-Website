import fresh_tomatoes
from fresh_tomatoes import open_movies_page


class Movie:
    #init function for creating a Movie object
    def __init__(self, title, youtubeurl, posterimageurl):
        self.title = title
        self.poster_image_url = posterimageurl
        self.trailer_youtube_url = youtubeurl

def get_movie_library():
    library = []
    #some of my favorite movies
    library.append(Movie("Me and You and Everyone We Know", "https://www.youtube.com/watch?v=2TTGhyp-mhE", "http://www.daedesign.com/wp-content/uploads/2011/04/blog_20060422.jpg"))
    library.append(Movie("Everything is Illuminated", "https://www.youtube.com/watch?v=l-hCtlNM32M", "http://www.argia.eus/blogak/gaizka-izagirre/wp-content/uploads/2014/11/753Everything_Is_Illuminated_CC_Custom_.jpg"))
    library.append(Movie("Eternal Sunshine of the Spotless Mind", "https://youtu.be/yE-f1alkq9I", "http://schmoesknow.com/wp-content/uploads/2014/08/poster-eternal-sunshine-of-the-spotless-mind.jpg"))
    library.append(Movie("Water for Elephants", "https://www.youtube.com/watch?v=_6b2XhXkPpg", "http://latimesblogs.latimes.com/.a/6a00d8341c630a53ef0147e0c60104970b-pi"))
    library.append(Movie("Willy Wonka and the Chocolate Factory", "https://www.youtube.com/watch?v=GNarV_3P4oM", "http://www.horacemann.org/uploaded/library/Cool_Stuff/Willy-Wonka-and-the-Chocolate-Factory-movie-poster-1020240284.jpg"))
    library.append(Movie("Little Miss Sunshine", "https://www.youtube.com/watch?v=wvwVkllXT80", "http://wfiles.brothersoft.com/l/little-miss-sunshine-poster_79877-1600x1200.jpg"))
    
    return library

def show_my_favorite_movies():
	#get list of favorite movies from library
    movies = get_movie_library()
	#render web page using fresh tomatoes function
    open_movies_page(movies)

#program starts running here:
show_my_favorite_movies()
    
    
