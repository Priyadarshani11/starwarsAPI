
"""pydantic models for films data coming from swapi.dev/api/films"""

from typing import List,Optional
from models.basemodel import Base

class film(Base):

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
