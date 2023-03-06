"""
The task 2 goes like following:
Pull data for the the first movie in star wars
Write the json data into a file named output.txt


SUBTASKS -
1. Output should be only list of names (first name & last name) of characters
in the movie.
2. Output should only print list of planet names used in the movie
3. Output should only print list of vehicle names used in the movie.
"""

import json
import requests
import argparse

from pprint import pprint
from typing import Dict, List

from utils.fetch_data import hit_url, fetch_data



FIRST_FILM_URL = "https://swapi.dev/api/films/1/"


def write_data_into_file(data: Dict) -> None:
    """writes dict data into a file"""

    with open("output.txt", "w") as fp:
        fp.write(json.dumps(data))


def first_task() -> Dict:
    """Returns a dict object from swapi.dev/api/films/1"""

    response = requests.get(FIRST_FILM_URL)
    result_ = response.json()
    write_data_into_file(result_)
    return result_


def main(data_: Dict)-> List:
    """
    Args:
        data_:

    Returns:

    """

    parser = argparse.ArgumentParser(

        prog='StarwarsAPI',

        usage="Fetches resources from swapi.dev based on "
              "whatever arguements we provide",

        description="It uses request library to get values from the swapi.dev",
    )
    # we are creating an option to provide resources

    parser.add_argument('-r',
                        '--resource',
                        default = "characters",
                        help='name of the resource',
                        choices=["characters", "starships", "vehicles", "planets"]
                        )
    arguments = parser.parse_args()
    print(f"parsed arguments are {arguments}")

    reso_data = data_.get(arguments.resource)  # returns None by default

    names = []
    for reso in reso_data:
        resource_data = hit_url(reso)
        resource_data = resource_data.json()
        names.append(resource_data.get("name"))

    return names


if __name__ == "__main__":

    # first task
    first_result = first_task()

    # second task
    second_result = main(first_result)
    pprint(second_result)




