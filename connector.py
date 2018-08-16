import requests

class Connector:
    def __init__(self):
        self.url = "https://www.leboncoin.fr/recherche"

    def get_ads(self, params):
        args = {
            'text': params.get('search-text')
        }

        response = requests.get(self.url, params=args)
        response.raise_for_status()

        return response