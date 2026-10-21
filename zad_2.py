class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka: {self.city}, ul. {self.street}, {self.zip_code}, godziny: {self.open_hours}, tel. {self.phone}"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date,
                 city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}, zatrudniony: {self.hire_date}"


class Book:
    def __init__(self, library, publication_date, author_name,
                 author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (
            f"Książka: {self.author_name} {self.author_surname}, "
            f"wydana: {self.publication_date}, "
            f"stron: {self.number_of_pages}\n"
            f"Biblioteka: {self.library}"
        )


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order:
    def __init__(self, employee, student, books: list[Book], order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_description = "\n".join(str(book) for book in self.books)

        return (
            f"Zamówienie z dnia: {self.order_date}\n"
            f"{self.employee}\n"
            f"Student: {self.student}\n"
            f"{books_description}"
        )


#biblioteki
library1 = Library("Katowice", "Bankowa 12", "40-007", "8:00-18:00", "123456789")
library2 = Library("Gliwice", "Akademicka 5", "44-100", "9:00-17:00", "987654321")


#pracownicy
employee1 = Employee("Anna", "Kowalska", "2020-01-10", "1985-05-20", "Katowice", "Polna 1", "40-001", "111111111")
employee2 = Employee("Jan", "Nowak", "2021-03-15", "1990-08-12", "Gliwice", "Leśna 2", "44-100", "222222222")
employee3 = Employee("Maria", "Wiśniewska", "2022-06-01", "1988-02-10", "Katowice", "Kwiatowa 3", "40-002", "333333333")


#studenci
student1 = Student("Klaudia", "Nowak")
student2 = Student("Piotr", "Kowalski")
student3 = Student("Adam", "Wiśniewski")


#książki
book1 = Book(library1, "2001", "J.K.", "Rowling", 320)
book2 = Book(library1, "1949", "George", "Orwell", 328)
book3 = Book(library1, "1997", "Andrzej", "Sapkowski", 400)
book4 = Book(library2, "1984", "Stephen", "King", 450)
book5 = Book(library2, "2010", "Olga", "Tokarczuk", 280)


#zamówienia
order1 = Order(employee1, student1, [book1, book2], "2026-10-20")
order2 = Order(employee2, student2, [book3, book4, book5], "2026-10-21")


print(order1)
print()
print(order2)