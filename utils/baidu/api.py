import requests


class Api:

    def __init__(self, auth) -> None:
        self.auth = auth

    def request(self, url, data):
        return requests.get(url, data=data)