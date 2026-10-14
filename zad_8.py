import requests
import argparse


class Brewery:
    def __init__(self, id, name, brewery_type, city, country, address, website):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.city = city
        self.country = country
        self.address = address
        self.website = website

    def __str__(self):
        return f"Nazwa: {self.name}, Typ: {self.brewery_type}, Miasto: {self.city}, Kraj: {self.country}, Adres: {self.address}, Strona: {self.website}"


parser = argparse.ArgumentParser()
parser.add_argument("--city")
args = parser.parse_args()

url = "https://api.openbrewerydb.org/v1/breweries"
parametry = {"per_page": 20}

if args.city:
    parametry["by_city"] = args.city

try:
    odpowiedz = requests.get(url, params=parametry)
    odpowiedz.raise_for_status()

    dane = odpowiedz.json()
    browary = []

    for b in dane:
        browar = Brewery(
            b["id"],
            b["name"],
            b["brewery_type"],
            b["city"],
            b["country"],
            b["address_1"],
            b["website_url"]
        )

        browary.append(browar)

    for b in browary:
        print(b)

except Exception as e:
    print("Blad:", e)