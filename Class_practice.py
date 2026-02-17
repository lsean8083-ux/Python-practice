class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, student_id: str|int, grade: list, major: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.grade = grade
        self.major = major

    def add_grades(self, new_grade):
        self.grade.append(new_grade)

    def average(self):
        if len(self.grade) == 0:
            return 0.0
        return sum(self.grade) / len(self.grade)


student = Person("sean", 15)
miko = Student("Miko", 16, 36648, [24, 24, 45, 556, 32], "Computer Science")



print(f"{miko.name}")
print(f"{student.name}")
print(f"{student.age}")


miko.add_grades(1001939)
print(f"{miko.average()}")

