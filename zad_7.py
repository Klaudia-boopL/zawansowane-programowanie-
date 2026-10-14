pip install requests
from dataclasses import dataclass
from typing import Optional
import requests

@dataclass
class Brewery:
    id: str
    name: str
    brewery_type: str
    address_1: Optional[str]
    address_2: Optional[str]
    address_3: Optional[str]
    city: str
    state_province: str
    postal_code: str
    country: str
    longitude: Optional[float]
    latitude: Optional[float]
    phone: Optional[str]
    website_url: Optional[str]
    state: str
    street: Optional[str]

    def __str__(self) -> str:
        return (
            f"Browar: {self.name}\n"
            f"ID: {self.id}\n"
            f"Typ: {self.brewery_type}\n"
            f"Adres: {self.address_1 or self.street or 'Brak danych'}\n"
            f"Miasto: {self.city}\n"
            f"Województwo/stan: {self.state_province}\n"
            f"Kod pocztowy: {self.postal_code}\n"
            f"Kraj: {self.country}\n"
            f"Szerokość geograficzna: {self.latitude}\n"
            f"Długość geograficzna: {self.longitude}\n"
            f"Telefon: {self.phone or 'Brak danych'}\n"
            f"Strona WWW: {self.website_url or 'Brak danych'}\n"
            f"Adres 2: {self.address_2 or 'Brak danych'}\n"
            f"Adres 3: {self.address_3 or 'Brak danych'}\n"
            f"Stan (pole starszego typu): {self.state}\n"
            f"{'-' * 50}"
        )

def main() -> None:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "per_page": 20,
        "page": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        breweries: list[Brewery] = [
            Brewery(**item) for item in data
        ]

        print(f"Pobrano {len(breweries)} browarów.\n")

        for brewery in breweries:
            print(brewery)

    except requests.RequestException as error:
        print(f"Błąd połączenia z API: {error}")
    except (ValueError, TypeError, KeyError) as error:
        print(f"Błąd przetwarzania danych: {error}")


if __name__ == "__main__":
    main()