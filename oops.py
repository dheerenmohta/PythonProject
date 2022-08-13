# students = {'name': 'd', "subject": "CSE", "grades": (66, 77, 88)}
#
# def avg(seequence):
#     return  sum(seequence)/len(seequence)
from typing import List
from main import named, named1, students, both


class Student:
    def __init__(self, name):
        self.name = name

    @classmethod
    def class_method(self):
        return "hello from class method"

    def __str__(self):
        # return "Hello"
        return f"Person name is : {self.name}"


class Enrolled_Student(Student):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = 3

    def __str__(self):
        return f"Name  is {super().__str__()} and age is {self.age}"


class Book:
    pass


class BookShelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self):
        return f"BookShelf has {len(self.books)} books"



if __name__ == '__main__':
    print(Student("A").name)
    print(Student("B"))
    print(Student.class_method())
    enrolled_Student = Enrolled_Student("C", 3)
    print(enrolled_Student)
    b1 = Book()
    b2 = Book()
    bookShelf = BookShelf([b1, b2])
    print(bookShelf)
    print(named(bookShelf = None))
    print(named1(**students))
    print(both(1,2,3,bookShelf = None))
    # print(avg(students["grades"]))
