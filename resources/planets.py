from resources.base import ResourceBase
from utils.fetch_data import hit_url
from utils.randgen import ProduceChars
from typing import Dict


class Planet(ResourceBase):
    """
    Planet class related functionality
    """

    def __init__(self) -> None:
        super().__init__()
        self.relative_url = "/api/planets"

    def get_count(self):
        complete_url = self.home_url + self.relative_url
        print("[INFO] count of planets")
        response = hit_url(complete_url)
        data = response.json()
        count = data.get("count")
        return count

    def get_sample_data(self, id_: int = 1) -> Dict:
        """
        Args:
            id_: sample id of the resource
        Returns:
            data (dict): output data from API endpoint.
        """

        absolute_url = self.home_url + self.relative_url + f"/{id_}"
        response = hit_url(absolute_url)
        data = response.json()
        return data

    def get_resource_urls(self):
        plural_url = self.home_url + self.relative_url
        print("[INFO] Fetching urls for planets")
        response = hit_url(plural_url)
        data = response.json()
        i = 0
        result = data.get("results")
        urls = []
        while i < len(result):
            url = data["results"][i]["url"]
            urls.append(url)
            i += 1
        return urls

    def get_random_urls_data(self):
        plural_url = self.home_url + self.relative_url
        print("[INFO] Fetching data from random planet url")
        response = hit_url(plural_url)
        data = response.json()
        n = len(data.get("results"))
        num = ProduceChars(0, n - 1, 1)
        for i in num:
            url_ = data["results"][i]["url"]
            response_ = hit_url(url_)
            data_ = response_.json()

        return data_






