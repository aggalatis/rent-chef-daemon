from bs4 import BeautifulSoup
import requests
from classes.helpers import *
from classes.database import *


class MainApp:
    def __init__(self):
        self.helpers = Helpers()
        self.helpers.delete_file()
        self.database = Database("db/database.db")
        start_url = "https://www.spitogatos.gr/pwliseis-katoikies/pollaples_perioxes-100,101,102,103,104,105,106,107/prwti_dimosieusi_24wres"
        has_pagination = True
        i = 1
        while has_pagination:
            current_url = start_url + "/selida_" + str(i)
            print("Checking page: " + str(i))
            res = requests.get(
                current_url,
                headers=self.helpers.get_headers())
            page_soup = BeautifulSoup(res.text, "html.parser")
            self.find_individual_ads(page_soup)
            has_pagination = self.find_last_pagination_page(page_soup)
            i += 1
        print("Done")



    def find_last_pagination_page(self, page_soup):
        ul_tags = page_soup.findAll("ul", {"class": "pagination"})
        if len(ul_tags) > 0:
            return True
        return False

    def find_individual_ads(self, page_soup):
        divs = page_soup.findAll("div", "searchListing")
        for div in divs:
            icon_divs = div.findAll("div", {"class": "tile-v5-sr__icons-icon"})
            for icon_div in icon_divs:
                if (icon_div.attrs['title'] == 'Αγγελία ιδιώτη'):
                    title = div.find("h4", {"class": "tile-v5-sr__title"})
                    self.append_ad_to_file(title.text[:-20].rstrip(), title.find("a").attrs['href'], div.find("div", {"class": "tile-v5-sr__location"}).text, div.find("span", {"class": "tile-v5-sr__details-price"}).text)
                    if self.database.select_ad_with_url(title.find("a").attrs['href']) is None:
                        self.database.insert_ad(title.text[:-20].rstrip().lstrip(), div.find("div", {"class": "tile-v5-sr__location"}).text, div.find("span", {"class": "tile-v5-sr__details-price"}).text, title.find("a").attrs['href'])

    def append_ad_to_file(self, title, link, area, price):
        print("Found ONE!!!!!!!!!")
        f = open('ads.txt', 'a')
        f.write(title + ", " + area + ", " + price + ", " + link)
        f.close()


if __name__ == "__main__":
    MainApp()
