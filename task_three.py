"""
1. TODO - import all resource classes here
2. TODO - get count of each resource
3. TODO - get singular resource URL from each resource
    - for example,
    - hit plural URL of starships and that will list all starships data
    - iterate on each starship data and capture singular URLs
    - all_starship_data = data.get("results")
    - you will iterate on `all_starship_data`,
4. TODO - pull data from random 3 "singular" resource URLs
    - utilize`utils` package to produce random 3 numbers from resource ids
    - and pull data for them
5. TODO - convert the script into CLI application
6. TODO - pretty print output (from pprint import pprint)

"""
from utils.randgen import ProduceChars
from pprint import pprint

# resource classes
from resources.films import Film
from resources.characters import Character
from resources.planets import Planet
from resources.species import Species
from resources.starships import Starship
from resources.vehicles import Vehicle


# pydantic classes (models)

from models.datamodels.characters import Character_
from models.datamodels.films import film
from models.datamodels.planets import Planet_
from models.datamodels.starships import Starship_
from models.datamodels.vehicles import Vehicle_
from models.datamodels.species import Species_

import argparse

def main():

    character_data = Character()
    film_data = Film()
    planets_data = Planet()
    species_data = Species()
    starships_data = Starship()
    vehicles_data = Vehicle()

    all_resource_object = [character_data, film_data, planets_data, species_data, starships_data, vehicles_data]

    """Task 2"""
    """ Count of all resources"""

    for resource in all_resource_object:
        data = resource.get_count()
        pprint(data)

    """ Task 3 """
    """ Singular URLs of all resources"""

    for resource in all_resource_object:
        result = resource.get_resource_urls()
        pprint(result)

    """Task 4 """
    """Pull data from random 3 "singular" resource URLs"""

    i = ProduceChars(0, (len(all_resource_object) - 1), 2)
    for j in i:
        resource = all_resource_object[j]
        result = resource.get_random_urls_data()
        pprint(result)

    """Task 5 """
    """ conversion of script into CLI application"""

    parser = argparse.ArgumentParser(

        prog = 'StarwarsAPI',

        usage = "Fetches resources from swapi.dev based on "
              "whatever arguements we provide",

        description = "It uses request library to get values from the swapi.dev",
    )
    # we are creating an option to provide resources

    parser.add_argument('-r',
                        '--resource',
                        default="people",
                        help='name of the resource',
                        choices=["characters", "starships", "vehicles", "planets","films"]
                        )

    parser.add_argument('-c', '--count', default=2,
                        help="count of random url")

    parser.add_argument('-s', '--start', default=0,
                        help="start of the range")

    parser.add_argument('-e', '--end', default=5,
                        help="end of the range")

    arguments = parser.parse_args()
    print(f"parsed arguments are {arguments}")

    if arguments.resource == "people":

        character_data = Character()


        count_of_characters = character_data.get_count()
        pprint(count_of_characters)

        all_singular_char_url = character_data.get_resource_urls()
        pprint((all_singular_char_url))

    elif arguments.resource == "planets":

        planets_data = Planet()


        count_of_planets = planets_data.get_count()
        pprint(count_of_planets)

        all_singular_planet_url = planets_data.get_resource_urls()
        pprint((all_singular_planet_url))

    elif arguments.resource == "starships":

        starships_data= Starship()


        count_of_starships = starships_data.get_count()
        pprint(count_of_starships)

        all_singular_starship_url = starships_data.get_resource_urls()
        pprint((all_singular_starship_url))

    elif arguments.resource == "vehicles":

        vehicles_data = Vehicle()

        count_of_vehicles = vehicles_data.get_count()
        pprint(count_of_vehicles)

        all_singular_vehicle_url = vehicles_data.get_resource_urls()
        pprint((all_singular_vehicle_url))

    elif arguments.resource == "films":

        film_data = Film()

        count_of_films = film_data.get_count()
        pprint(count_of_films)

        all_singular_film_url = film_data.get_resource_urls()
        pprint((all_singular_film_url))

    obj = ProduceChars(arguments.start,arguments.end,int(arguments.count))
    for i in obj:
        resource = all_resource_object[i]
        result = resource.get_random_urls_data()
        pprint(result)


if __name__ == "__main__":

    main()











