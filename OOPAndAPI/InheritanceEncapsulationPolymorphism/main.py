def avg(dct):
    sum_grades = 0
    for item in dct.values():
        sum_grades += sum(item) / len(item)
    return sum_grades / len(dct.values())


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задание: {avg(self.grades)}\n' \
               f'Курсы в прцессе обучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surmame):
        super().__init__(name, surmame)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg(self.grades)}'

    def __lt__(self, other):
        return avg(self.grades) < avg(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


student = Student('student', 'Eman', 'your_gender')
student.courses_in_progress += ['Python']
student.courses_in_progress += ['Python1']

student1 = Student('student1', 'Eman', 'your_gender')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Python1']

lecturer = Lecturer('lecturer', 'Eman')
lecturer.courses_attached += ['Python']
lecturer.courses_attached += ['Python1']

lecturer1 = Lecturer('lecturer1', 'Eman')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['Python1']

reviewer = Reviewer('reviewer', 'Eman')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Python1']

reviewer1 = Reviewer('reviewer1', 'Eman')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Python1']

student.rate(lecturer, 'Python', 10)
student1.rate(lecturer, 'Python', 5)
student.rate(lecturer, 'Python1', 5)
student1.rate(lecturer, 'Python1', 10)

student.rate(lecturer1, 'Python', 10)
student1.rate(lecturer1, 'Python', 4)
student.rate(lecturer1, 'Python1', 5)
student1.rate(lecturer1, 'Python1', 10)

reviewer.rate(student, 'Python', 1)
reviewer1.rate(student, 'Python', 5)
reviewer.rate(student, 'Python1', 5)
reviewer1.rate(student, 'Python1', 10)

reviewer.rate(student1, 'Python', 10)
reviewer1.rate(student1, 'Python', 5)
reviewer.rate(student1, 'Python1', 5)
reviewer1.rate(student1, 'Python1', 10)


print(lecturer)
print(lecturer1)
print(student)
print(student1)
print(reviewer)
print(reviewer1)

print(student < student1)

print(lecturer < lecturer1)






