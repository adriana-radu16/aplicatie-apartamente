import requests
from bs4 import BeautifulSoup
import datetime

class Scraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        }

    def get_olx(self, city="targoviste"):
        url = f"https://www.olx.ro/imobiliare/apartamente-garsoniere-de-vanzare/?q={city}"
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        ads = soup.find_all("div", class_="css-1sw7q4x")
        results = []
        for ad in ads:
            try:
                title = ad.find("h6").text.strip()
                price = ad.find("p", class_="css-10b0gli er34gjf0").text.strip()
                link = ad.find("a", href=True)["href"]
                date_info = ad.find("span", class_="css-19yf5ek").text.strip()

                results.append({
                    "Titlu": title,
                    "Preț": price,
                    "Link": link,
                    "Dată": date_info,
                    "Nou": "azi" in date_info.lower() or "ieri" in date_info.lower(),
                    "Sursă": "OLX"
                })
            except:
                continue
        return results

    def get_publi24(self, city="targoviste"):
        url = f"https://www.publi24.ro/anunturi/imobiliare/apartamente-de-vanzare/{city}/"
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        ads = soup.find_all("div", class_="listing-item")
        results = []
        for ad in ads:
            try:
                title = ad.find("h4").text.strip()
                price = ad.find("div", class_="price").text.strip()
                link = ad.find("a", href=True)["href"]

                results.append({
                    "Titlu": title,
                    "Preț": price,
                    "Link": link,
                    "Dată": "N/A",
                    "Nou": False,
                    "Sursă": "Publi24"
                })
            except:
                continue
        return results

    def get_listings(self, city="targoviste"):
        listings = []
        listings.extend(self.get_olx(city))
        listings.extend(self.get_publi24(city))
        # Aici putem adăuga get_storia() și get_imobiliare()
        return listings


scraper = Scraper()
