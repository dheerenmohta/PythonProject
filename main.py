# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

students = {'name': 'd', "subject": "CSE", "grades": (66, 77, 88)}


def find_avg_grades(data):
    grades = students["grades"]
    return sum(grades) / len(grades)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    l = ["a", 1, 2]
    t = (1, 2, 3)
    s = {1, 2, 1}

    print(2 in (1, 2))

    print(l, t, s)

    for i in l:
        print(f'{i} in l')

    print(round(sum(t) / 7, 5))

    numbers = [1, 2, 3]
    doubles = [num * 2 for num in numbers]
    print(numbers)
    print(doubles)

    friends = ["a", "b", "c", "s", "ss", "sss"]
    friendStartWithS = [friend for friend in friends if friend.startswith("s")]
    print(friendStartWithS)

    students = {"a": 1, "b": 2, "c": 3}
    for student in students:
        print(f'{student} has id {students[student]}')

    for student, rollNo in students.items():
        print(f"{student} :{rollNo}")

    get_student_details(students)

    #
    # while True:
    #     user_input =  input("You want to plau y/n ")
    #     if user_input == "n":
    #         break


def double(x):
    return x * 2


def get_student_details(students):
    if "a" in students:
        print(f'{"a"} has id {students["a"]}')
    students = [("a", 1, "Delhi"), ("b", 2, "Agra"), ("c", 3, "Mathura")]

    for name, rollNo, city in students:
        print(f"name {name} rollNo {rollNo} city {city}")
    head, *tail = [("a", 1, "Delhi"), ("b", 2, "Agra"), ("c", 3, "Mathura")]
    print(head)
    print(tail)

    double_list = [double(x) for x in (1, 2, 3)]
    print(double_list)

    d_list = [(lambda x: x * 2)(x) for x in (1, 2, 3)]
    print(d_list)

    d_list2 = list(map(lambda x: x * 3, [1, 2, 3]))
    print(d_list2)

    people_dict = {student[1]: student for student in students}
    print(people_dict)


def multiply(*args):
    total = 1
    for arg in args:
        total = total * arg

    return total


def apply(*args, operator) -> object:
    if operator == "*":
        return multiply(*args)


def named(**kwargs):
    print(kwargs)


def named1(name, subject, grades):
    print(name, subject, grades)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = "Hello {}  today is {}"
    print_hi(name.format("Dheeren", "tue"))
    print(find_avg_grades(students))
    print(apply(1, 2, 3, operator="*"))
    named(x=1, y=2)
    named1(**students)
    named(**students)
    both(1,2,3,name="a",age= 2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
