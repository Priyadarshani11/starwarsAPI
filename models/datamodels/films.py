
"""pydantic models for films data coming from swapi.dev/api/films"""

from pydantic import BaseModel
from typing import List,Optional

class film(BaseModel):

    title : str
    episode_id : int
    opening_crawl : str
    director : str
    producer : str
    release_date : str

    species : Optional[List[str]]
    characters : Optional[List[str]]
    planets : Optional[List[str]]
    starships : Optional[List[str]]
    vehicles : Optional[List[str]]


# if __name__ == "__main__":
#
#     data = {
#         "title": "A New Hope",
#         "episode_id": 4,
#         "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, "
#                          "have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring "
#                          "the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate ",
#         "director": "George Lucas",
#         "producer": "Gary Kurtz, Rick McCallum",
#         "release_date": "1977-05-25",
#         "characters": [
#             "https://swapi.dev/api/people/1/",
#             "https://swapi.dev/api/people/2/",
#
#         ],
#         "planets": [
#             "https://swapi.dev/api/planets/1/",
#             "https://swapi.dev/api/planets/2/",
#             "https://swapi.dev/api/planets/3/"
#         ],
#         "starships": [
#             "https://swapi.dev/api/starships/2/",
#             "https://swapi.dev/api/starships/3/",
#
#         ],
#         "vehicles": [
#             "https://swapi.dev/api/vehicles/4/",
#             "https://swapi.dev/api/vehicles/6/",
#
#         ],
#         "species": [
#             "https://swapi.dev/api/species/1/",
#             "https://swapi.dev/api/species/2/",
#
#         ],
#         "created": "2014-12-10T14:23:31.880000Z",
#         "edited": "2014-12-20T19:49:45.256000Z",
#         "url": "https://swapi.dev/api/films/1/"
#     }
#
#
#
#     obj = film(**data)
#     print(obj)
#     breakpoint()






