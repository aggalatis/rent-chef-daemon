from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
res = requests.get("https://www.spitogatos.gr/pwliseis-katoikies/glyfada/prwti_dimosieusi_24wres", headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
results = soup.findAll("div", {"class": "searchListing"})

for item in results:
    print(item.find("h4", {"class": "tile-v5-sr__title"}).text)

