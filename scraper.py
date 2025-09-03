import datetime
import random

class Scraper:
    def __init__(self):
        # aici putem defini lista de site-uri suportate
        self.sources = [
            "https://www.olx.ro/imobiliare",
            "https://www.storia.ro",
            "https://www.imobiliare.ro",
            "https://www.publi24.ro/anunturi/imobiliare",
            "https://www.piata-az.ro",
        ]

    def get_listings(self, city="Târgoviște"):
        today = datetime.datetime.now()

        # 🔹 momentan simulează extragerea (poți extinde cu requests + BeautifulSoup)
        listings = []
        for i in range(10):
            listing = {
                "Titlu": f"Apartament {random.randint(1, 4)} camere - {city}",
                "Preț": f"{random.randint(40, 120)}.000 €",
                "Suprafață": f"{random.randint(40, 100)} mp",
                "An construcție": random.choice([1990, 2005, 2015, 2020, 2023]),
                "Sursă": random.choice(self.sources),
                "Dată": today.strftime("%Y-%m-%d %H:%M"),
                "Nou": True if (today - datetime.timedelta(hours=random.randint(1, 48))) < today else False
            }
            listings.append(listing)

        return listings


scraper = Scraper()
