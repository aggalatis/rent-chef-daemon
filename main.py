from bs4 import BeautifulSoup
import requests
import time
from classes.helpers import *
from classes.database import *
from nordvpn_switcher import *


class MainApp:
    def __init__(self):
        initialize_VPN(save=1, area_input=['random countries europe 20'])
        rotate_VPN()
        time.sleep(30)
        self.helpers = Helpers()
        self.helpers.delete_file()
        self.database = Database("db/database.db")
        start_url = "https://www.spitogatos.gr/pwliseis-katoikies/pollaples_perioxes-100,101,102,103,104,105,106,107,108,109,110,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198/prwti_dimosieusi_24wres"
        maximum_page = self.find_last_page_from_link(start_url)
        should_iterate = True
        found_ad = True
        i = maximum_page
        last_iteration_found = True

        while should_iterate:
            current_url = start_url + "/selida_" + str(i)
            print("Checking page: " + str(i))
            res = requests.get(
                current_url,
                headers=self.helpers.get_headers())
            page_soup = BeautifulSoup(res.text, "html.parser")
            this_iteration_found = self.find_individual_ads(page_soup)
            i -= 1
            if this_iteration_found == False and last_iteration_found == False:
                should_iterate = False
            else:
                should_iterate = True
            last_iteration_found = this_iteration_found
        self.database.close_connection()
        print("Done")

    
    def find_last_page_from_link(self, start_url):
        init_req = requests.get(
                start_url,
                headers=self.helpers.get_headers()
        )
        first_soup = BeautifulSoup(init_req.text, "html.parser")
        last_li_tag = first_soup.find("li", {"class", "last"})
        last_anchor = last_li_tag.find("a")
        link_seagments = last_anchor.attrs['href'].split('/');
        splitted_selida = link_seagments[len(link_seagments) -1].split('_')
        print(f'Last page is: {splitted_selida[1]} but i will search one more' )
        return int(splitted_selida[1])
    

    def find_last_pagination_page(self, page_soup):
        ul_tags = page_soup.findAll("ul", {"class": "pagination"})
        if len(ul_tags) > 0:
            return True
        return False

    def find_individual_ads(self, page_soup):
        divs = page_soup.findAll("div", "searchListing")
        flag = False
        for div in divs:
            icon_divs = div.findAll("div", {"class": "tile-v5-sr__icons-icon"})
            for icon_div in icon_divs:
                if (icon_div.attrs['title'] == 'Αγγελία ιδιώτη'):
                    flag = True
                    title = div.find("h4", {"class": "tile-v5-sr__title"})
                    self.helpers.append_ad_to_file(title.text[:-20].rstrip(), title.find("a").attrs['href'], div.find("div", {"class": "tile-v5-sr__location"}).text, div.find("span", {"class": "tile-v5-sr__details-price"}).text)
                    if self.database.select_ad_with_url(title.find("a").attrs['href']) is None:
                        self.database.insert_ad(title.text[:-20].rstrip().lstrip(), div.find("div", {"class": "tile-v5-sr__location"}).text, div.find("span", {"class": "tile-v5-sr__details-price"}).text, title.find("a").attrs['href'])
        return flag



if __name__ == "__main__":
    MainApp()
