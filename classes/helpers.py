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
            'Connection': 'keep-alive',
            'cache-control': 'no-cache',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'upgrade-insecure-requests': '1',
            'pragma': 'no-cache'
        }
        return headers

    def get_proxy(self):
        proxy = 'https://213.6.28.69:5678'
        return proxy

    def delete_file(self):
        if (path.exists("ads.txt")):
            os.remove("ads.txt")

    def get_proxies(self):
        response = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=50&page=2&sort_by=lastChecked&sort_type=desc&protocols=https')
        proxies_total = json.loads(response.text)
        proxies = proxies_total['data']
        return_proxies = []
        for proxy in proxies:
            return_proxies.append(proxy['ip'] + ':' + proxy['port'])
        return return_proxies

    def append_ad_to_file(self, title, link, area, price):
        f = open('ads.txt', 'a')
        f.write(title + ", " + area + ", " + price + ", " + link)
        f.close()

    def append_to_file(self, message):
        f = open('ads.txt', 'a')
        f.write(message)
        f.close()

    def check_working_proxies(self, proxies):
        for proxy in proxies:
            try:
                res = requests.get(
                    'https://www.spitogatos.gr/pwliseis-katoikies/pollaples_perioxes-100,101,102,103,104,105,106,107,108,109,110,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198/prwti_dimosieusi_24wres',
                    proxies={'http': 'http://' + proxy, 'https': 'https://' + proxy},
                    headers=self.get_headers(),
                    timeout=2
                )
                print(res.text)
                self.append_to_file("working: " + proxy)
                print("working:", proxy)
            except:
                print("failed:", proxy)
                pass
        exit()
