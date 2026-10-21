class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        percentage = average / 5 * 100
        return percentage > 50


s1 = Student("Klaudia", [4, 5, 3])
s2 = Student("Rysiu", [2, 2, 2])

print(s1.is_passed())
print(s2.is_passed())