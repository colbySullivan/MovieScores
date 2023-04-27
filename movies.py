import imdb

"""
   author = Colby Sullivan, Last modified 4/26/2023
"""

def get_movies():
    list_of_movies = list()
    ia = imdb.IMDb()
    items = ia.search_movie('Avengers')
    for i in items:
        list_of_movies.append(i)

##########################################################################

def main(num_to_show):
    get_movies

if __name__ == '__main__':
     main()
