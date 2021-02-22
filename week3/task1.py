import random
class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade():
        grades = self.data_sheet.get_grades_as_list()
        return (sum(grades)/len(grades))


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list():
        return [value for value.grade in self.courses]


class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade)
    self.name = name
    self.classroom = classroom
    self.teacher = teacher
    self.ETCS = ETCS
    self.grade = grade

def makeStudents(amount):
    names = ["John", "Svend", "Henrik", "Jørgen", "Jens", "Bent", "Joan", "Joachim"]
    gender = ["boy", "girl", "odder"]
    grades = [-3, 00, 2, 4, 7, 10, 12]
    imgurl = "pancake.img"
    c1 = Course("Matematik", "a1", "svend bent", "10", "?")
    c2 = Course("Dansk", "a2", "jørgen jetjæger", "20", "?")
    c3 = Course("Svensk", "a3", "henrik hapengut", "10", "?")
    c4 = Course("Tysk", "a4", "svend sved", "10", "?")
    courses = [c1, c2, c3, c4]
    students = [Student(random) for amount

makeStudents(4)