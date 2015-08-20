__author__ = 'Sylvestre'

MOVIES_DATA = [
               ('Leon: The Professional', 'http://ia.media-imdb.com/images/M/MV5BMTgzMzg4MDkwNF5BMl5BanBnXkFtZTcwODAwNDg3OA@@._V1_SY317_CR4,0,214,317_AL_.jpg', 'https://www.youtube.com/watch?v=ns4vh_xAn98'),
               ('25th Hour', 'http://ia.media-imdb.com/images/M/MV5BMTUxNDEyNjE4OF5BMl5BanBnXkFtZTYwNTMyNjU3._V1_SX214_AL_.jpg', 'https://www.youtube.com/watch?v=-GL6VFadJ9k'),
               ('Bringing Out the Dead', 'http://ia.media-imdb.com/images/M/MV5BMTQ4MjgzMDc1Nl5BMl5BanBnXkFtZTYwOTc5ODk4._V1_SY317_CR7,0,214,317_AL_.jpg', 'https://www.youtube.com/watch?v=sfUwvmRmMtw')
               ]

movies = list()

#A Python class to store movie's data.
class movie:
    title = ''
    poster_image_url = ''
    trailer_youtube_url = ''


    def save(self):
        """
        Add Movie instance to the global variable movies.
        :return: List
        """
        global movies
        movies.append(self)
        return movies

#Loop over the nested list in our ou MOVIES_DATA tuple
for m in MOVIES_DATA:
    f = movie()                     #Initialize a movie instance.
    f.title = m[0]                  #Populate movie instance attribute with corresponding data from the nested list.
    f.poster_image_url = m[1]
    f.trailer_youtube_url = m[2]
    f.save()                        #Add the movie instance to the global movie list.


from fresh_tomatoes import open_movies_page
open_movies_page(movies)            #Create the page using the generated list.



