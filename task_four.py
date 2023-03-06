"""
TODO
1. Pull data for the first movie ("A New Hope") and save in DB.
2. Replace the data for each endpoint listed in the JSON object and insert
that data into database table
For example - "A new hope" movie has following resource endpoints -
- characters 15
- planets  7
- starships   10
- vehicles  5
- species  40
"""

from resources.films import Film   # resource model
from models.datamodels.films import film # pydantic model
from models.datamodels.characters import Character_ # pydantic model
from models.datamodels.planets import Planet_ # resorce model
from models.datamodels.vehicles import  Vehicle_
from models.datamodels.starships import Starship_
from models.datamodels.species import Species_
from utils.fetch_data import hit_url
from dal.db_conn_helper import get_db_conn
from dal.dml import insert_resource
from utils.timing import timeit



data = Film().get_sample_data(id_=1)
film_data = film(**data)

@timeit
def insert_film_data():

    # create DB connection
    conn = get_db_conn()

    film_columns = [
        "title",
        "opening_crawl",
        "director",
        "producer",
        "release_date",
        "created",
        "edited",
        "url",
    ]

    film_values = [
        film_data.title,
        film_data.opening_crawl,
        film_data.director,
        film_data.producer,
        film_data.release_date,
        film_data.created.strftime("%y-%m-%d"),
        film_data.edited.strftime("%y-%m-%d"),
        film_data.url,
    ]
    result = insert_resource(
        "film", "film_id", film_data.episode_id, film_columns, film_values
    )

@timeit
def insert_char_data():

    data = film_data.characters
    for i in data:
        response = hit_url(i)
        response = response.json()

        char_data = Character_(**response)

        # create DB connection

        conn = get_db_conn()

        char_columns = [
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",

        ]

        char_values = [
            char_data.name,
            char_data.height,
            char_data.mass,
            char_data.hair_color,
            char_data.skin_color,
            char_data.eye_color,
            char_data.birth_year,
            char_data.gender,
            char_data.homeworld,

        ]

        char_id = int(char_data.url.split("/")[-2])
        result = insert_resource(
            "characters", "char_id", char_id, char_columns, char_values
        )

def insert_planet_data():

    data = film_data.planets
    for i in data:
        response = hit_url(i)
        response = response.json()

        planet_data = Planet_(**response)
            # create DB connection

        conn = get_db_conn()

        planet_columns = [
                "climate",
                "diameter",
                "gravity",
                "name",
                "orbital_period",
                "population",
                "rotation_period",
                "surface_water",
                "terrain"
            ]

        planet_values = [
                planet_data.climate,
                planet_data.diameter,
                planet_data.gravity,
                planet_data.name,
                planet_data.orbital_period,
                planet_data.population,
                planet_data.rotation_period,
                planet_data.surface_water,
                planet_data.terrain
            ]

        planet_id = int(planet_data.url.split("/")[-2])
        result = insert_resource(
                "planet", "planet_id", planet_id, planet_columns, planet_values
            )

def insert_vehicle_data():

    data = film_data.vehicles
    for i in data:
        response = hit_url(i)
        response = response.json()

        vehicle_data =Vehicle_(**response)

        # create DB connection
        conn = get_db_conn()

        vehicle_columns = [
            "cargo_capacity",
            "consumables",
            "cost_in_credits",
            "crew",
            "length",
            "manufacturer",
            "max_atmosphering_speed",
            "model",
            "name",
            "passengers",
            "vehicle_class"
        ]

        vehicle_values = [
            vehicle_data.cargo_capacity,
            vehicle_data.consumables,
            vehicle_data.cost_in_credits,
            vehicle_data.crew,
            vehicle_data.length,
            vehicle_data.manufacturer,
            vehicle_data.max_atmosphering_speed,
            vehicle_data.model,
            vehicle_data.name,
            vehicle_data.passengers,
            vehicle_data.vehicle_class
        ]

        vehicle_id = int(vehicle_data.url.split("/")[-2])
        result = insert_resource(
            "vehicle", "vehicle_id", vehicle_id, vehicle_columns, vehicle_values
        )
def insert_starship_data():

    data = film_data.starships
    for i in data:
        response = hit_url(i)
        response = response.json()

        starship_data = Starship_(**response)
        # create DB connection

        conn = get_db_conn()

        starship_columns = [
            "MGLT" ,
            "cargo_capacity",
            "consumables",
            "cost_in_credits",
            "crew",
            "hyperdrive_rating",
            "length",
            "manufacturer",
            "max_atmosphering_speed",
            "model",
            "name",
            "starship_class",
            "passengers",
        ]

        starship_values = [
            starship_data.MGLT,
            starship_data.cargo_capacity,
            starship_data.consumables,
            starship_data.cost_in_credits,
            starship_data.crew,
            starship_data.hyperdrive_rating,
            starship_data.length,
            starship_data.manufacturer,
            starship_data.max_atmosphering_speed,
            starship_data.model,
            starship_data.name,
            starship_data.starship_class,
            starship_data.passengers,

        ]

        starship_id = int(starship_data.url.split("/")[-2])
        result = insert_resource(
            "starship", "starship_id", starship_id, starship_columns, starship_values
        )

def insert_species_data():

    data = film_data.species
    for i in data:
        response = hit_url(i)
        response = response.json()

        species_data = Species_(**response)

        # create DB connection

        conn = get_db_conn()

        species_columns = [
             "average_height",
             "average_lifespan",
             "classification",
             "designation",
             "eye_colors",
             "hair_colors",
             "name",
             "skin_colors"
        ]

        species_values = [
             species_data.average_height,
             species_data.average_lifespan,
             species_data.classification,
             species_data.designation,
             species_data.eye_colors,
             species_data.hair_colors,
             species_data.name,
             species_data.skin_colors
        ]

        species_id = int(species_data.url.split("/")[-2])

        result = insert_resource(
            "species", "species_id", species_id, species_columns, species_values
        )


if __name__ == "__main__":
     insert_char_data()
     insert_planet_data()
     insert_vehicle_data()
     insert_starship_data()
     insert_species_data()










