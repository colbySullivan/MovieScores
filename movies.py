from imdb import Cinemagoer #https://cinemagoer.readthedocs.io/en/latest/usage/index.html
import sys

"""
   author = Colby Sullivan, Last modified 4/27/2023
"""

def get_similar_movies(list_of_movies, ia):
    similar_titles = ia.search_movie('Twins')
    for movie in similar_titles:
        only_titles = movie.get('title')
        #rating = similar_titles[i].get('rating')
        list_of_movies.append(only_titles)
    return list_of_movies

def get_best_worst_movies(list_of_movies, imdb_movies, number_of_movies):
    list_of_movies = list()
    for i in range(number_of_movies):
        title = imdb_movies[i].get('title')
        rating = imdb_movies[i].get('rating')
        list_of_movies.append(title)
    return list_of_movies

##########################################################################

def main(user_action):
    list_of_movies = list()
    ia = Cinemagoer()
    number_of_movies = 2
    if user_action == 1:
        print(get_similar_movies(list_of_movies, ia))
        return 1
    elif user_action == 2:
        imdb_movies = ia.get_bottom100_movies() #TODO If statement
    else:
        imdb_movies = ia.get_top250_movies()
    print(get_best_worst_movies(list_of_movies, imdb_movies, number_of_movies))

if __name__ == '__main__':
    # Verify proper command line arguments
    if len(sys.argv) != 2 or any(not char.isdigit() for char in sys.argv[1]):
        print("Exactly one numeric argument is required")
        print("Example: python movies.py 1")
        quit()

    user_action = int(sys.argv[1])
    main(user_action)
