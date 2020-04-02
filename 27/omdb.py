import json


def get_movie_data(files: list) -> list:
    """Parse movie json files into a list of dicts"""   
    movies = []
    for fi in files:    # because the original list is bundled into files
        with open(fi) as f:     # I guess the need to use a 'with' statement is to be able to 
            json_ = json.loads(f.read())    # close the file after it is done
        movies.append(json_)    # remember that json.loads already converts to dict_
    return movies


def get_single_comedy(movies: list) -> str:
    """return the movie with Comedy in Genres"""
    


def get_movie_most_nominations(movies: list) -> str:
    """Return the movie that had the most nominations"""
    pass


def get_movie_longest_runtime(movies: list) -> str:
    """Return the movie that has the longest runtime"""
    pass
