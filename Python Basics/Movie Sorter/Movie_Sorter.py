import os
import imdb


def get_video_files():
    files = []
    extensions = (".mkv", ".mp4", ".avi", ".mov")

    # os.listdir() returns a list of names of all files and folders inside the current directory
    for path in os.listdir():
        if os.path.isfile(path) and path.endswith(extensions):
            files.append(path)

    return files

# function to get the name and year of the movie that's given
def get_movie_info(filename):
    ia = imdb.IMDb()
    print(filename)
    search_term = input("Enter query: ")
    movies = ia.search_movie(search_term)
    for index, movie in enumerate(movies):
        print(f"{index}. {movie['title']} ({movie['year']})")
    selection = int(input("Enter the correct movie: "))
    movie = movies[selection]
    title = movie['title']
    year = movie['year']
    movie = f"{title} ({year})"
    print(movie)
    return movie