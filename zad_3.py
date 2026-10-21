class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"Dom:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m2\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zł\n"
            f"Powierzchnia działki: {self.plot} m2"
        )


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Mieszkanie:\n"
            f"Adres: {self.address}\n"
            f"Powierzchnia: {self.area} m2\n"
            f"Liczba pokoi: {self.rooms}\n"
            f"Cena: {self.price} zł\n"
            f"Piętro: {self.floor}"
        )


# Tworzenie obiektów
house1 = House(150, 5, 850000, "Katowice, ul. Leśna 10", 600)
flat1 = Flat(60, 3, 450000, "Katowice, ul. Kwiatowa 5", 2)

# Wyświetlenie obiektów
print(house1)
print()
print(flat1)