class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Введение в программированеи"]
        self.courses_in_progress = ["Python", "Git"]
        self.courses_attached = ["Введение в программированеи", "Python", "Git"]
        self.grades = {}

# Метод выставления оценок Лекторам классом Student
# (оценки по 10-ти бальной шкале хранятся в атрибуте словаре у Lectorer
# в котором ключи - это название курсов, а значения - это список оценок).
# Lecturer при этом должен быть закреплен за тем курсом, на который записан студент
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Parents:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Parents):
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Введение в программированеи"]
        self.courses_in_progress = ["Python", "Git"]
        self.courses_attached = ["Введение в программированеи", "Python", "Git"]
        self.grades = {"Введение в программированеи": [8,9,10,9,9], "Python": [10,9,9,9,8], "Git": [9,10,10,10,10]}
# Метод выставления оценок Лекторам классом Student
# (оценки по 10-ти бальной шкале хранятся в атрибуте словаре у Lectorer
# в котором ключи - это название курсов, а значения - это список оценок).
# Lecturer при этом должен быть закреплен за тем курсом, на который записан студент


class Reviewer(Parents):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ["Введение в программированеи","Python", "Git"]

    # Метод выставления оценок Студентам классом Reviewer
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
# пишем след 2 строчки для тех "кому" выставляют оценки (Student, Lecturer)

#best_student = Student('Ruoy', 'Eman', 'your_gender')
#best_student.courses_in_progress += ['Python']

#best_lecturer = Lecturer('Jhon', 'Nik', 'your_gender')
#best_lecturer.courses_in_progress += ['Python']

#cool_reviewer = Parents('Some', 'Buddy')
#cool_reviewer.courses_attached += ['Python']
#
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)
#cool_mentor.rate_hw(best_student, 'Python', 10)

#print(best_student.grades)

# задание 3
 def_str_(self):
   res = f"Имя: {111111}"
