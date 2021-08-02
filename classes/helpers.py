import os
from os import path
import requests
import json

class Helpers:
    def get_headers(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        }
        return headers

    def get_proxy(self):
        proxy = 'https://213.6.28.69:5678'
        return proxy

    def delete_file(self):
        if (path.exists("ads.txt")):
            os.remove("ads.txt")

    def append_ad_to_file(self, title, link, area, price):
        f = open('ads.txt', 'a')
        f.write(title + ", " + area + ", " + price + ", " + link)
        f.close()

    def get_url_from_file(self):
        file = open('files/spitogatos.file', mode='r')
        my_url = file.read();
        file.close()
        return my_url

