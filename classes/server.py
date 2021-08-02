import requests
from classes.helpers import *


class Server:
    def __init__(self):
        self.server_API = 'http://174.138.4.153:30546'
        self.helpers = Helpers()

    def post_ad(self, title, area, price, link):
        ad = {
            "title": title,
            "area": area,
            "price": price,
            "link": link,
            "website": "spitogatos.gr"
        }
        r = requests.post(
            f'{self.server_API}/Ad/Create',
            json=ad,
            headers=self.helpers.get_headers()
        )
        print(r.json())
