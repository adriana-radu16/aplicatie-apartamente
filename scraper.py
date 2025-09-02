# Simulare scraper pentru anunțuri
# În realitate, ar trebui conectat la OLX, Publi24, Imobiliare etc.

import datetime

def get_listings(city="Târgoviște"):
    today = datetime.datetime.now()
    return [
        {
            "Titlu": "Apartament 2 camere Micro 9",
            "Preț": "55,000 EUR",
            "Micro": "Micro 9",
            "Dată publicare": (today - datetime.timedelta(hours=30)).strftime("%Y-%m-%d %H:%M"),
            "Dată reînnoire": today.strftime("%Y-%m-%d %H:%M"),
            "Link": "https://www.olx.ro/example-apartament1",
            "An construcție": "1985",
            "Nou": (today - datetime.timedelta(hours=30)).days < 2
        },
        {
            "Titlu": "Apartament 3 camere Micro 6",
            "Preț": "72,000 EUR",
            "Micro": "Micro 6",
            "Dată publicare": (today - datetime.timedelta(days=3)).strftime("%Y-%m-%d %H:%M"),
            "Dată reînnoire": (today - datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M"),
            "Link": "https://www.imobiliare.ro/example-apartament2",
            "An construcție": "Nou",
            "Nou": False
        }
    ]
