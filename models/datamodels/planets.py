
"""
This module defines pydantic (provides Py3 data-classes validation out of the box) models used
for validation and (de)serialization in API requests/responses.
"""

from typing import List, Optional

from models.basemodel import Base


class Planet_(Base):
    """Pydantic model class meant to validate the data for `Planet` object from
    single resource endpoint from starwars API.
    """

    # attribute fields
    climate: str
    diameter: str
    gravity: str
    name: str
    orbital_period: str
    population: str
    rotation_period: str
    surface_water: str
    terrain: str

# if __name__ == "__main__":
#     data = {
#     "name": "Tatooine",
#     "rotation_period": "23",
#     "orbital_period": "304",
#     "diameter": "10465",
#     "climate": "arid",
#     "gravity": "1 standard",
#     "terrain": "desert",
#     "surface_water": "1",
#     "population": "200000",
#     "residents": [
#         "https://swapi.dev/api/people/1/",
#         "https://swapi.dev/api/people/2/",
#         "https://swapi.dev/api/people/4/",
#
#     ],
#     "films": [
#         "https://swapi.dev/api/films/1/",
#         "https://swapi.dev/api/films/3/",
#
#     ],
#     "created": "2014-12-09T13:50:49.641000Z",
#     "edited": "2014-12-20T20:58:18.411000Z",
#     "url": "https://swapi.dev/api/planets/1/"
# }
#     obj = Planet_(**data)
#     print(obj)
#     breakpoint()