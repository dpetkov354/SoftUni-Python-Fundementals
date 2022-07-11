students = {}

n = int(input())

for _ in range(n):
    student_name = input()
    student_grade = float(input())
    if student_name not in students:
        students[student_name] = [student_grade]
    else:
        students[student_name].append(student_grade)

filtered_students = {}

for student_name, student_grades in students.items():
    av_grade = sum(student_grades) / len(student_grades)
    if av_grade >= 4.50:
        filtered_students[student_name] = av_grade

result = []
for student_name, av_grade in sorted(filtered_students.items(), key=lambda x: -x[1]):
    result.append(f'{student_name} -> {av_grade:.2f}')
print('\n'.join(result))




# class Student:
#     def __init__(self, name: str) -> None:
#         self.name = name
#         self.grades = []
#         self.av_grade = 0
#
#     def add_grade(self, grade):
#         self.grades.append(grade)
#
#
# class Academy:
#     def __init__(self) -> None:
#         self.students = []
#         self.filtered = []
#
#     def enroll(self, name: str, grade: float):
#         new_student = True
#         for s in self.students:
#             if s.name == name:
#                 new_student = False
#                 s.add_grade(grade)
#         if new_student:
#             student = Student(name)
#             student.add_grade(grade)
#             self.students.append(student)
#
#     def filter(self, THRESHOLD: float):
#         for student in self.students:
#             student.av_grade += sum(student.grades)/len(student.grades)
#             if student.av_grade >= THRESHOLD:
#                 self.filtered.append(student)
#
#     def __repr__(self) -> str:
#
#         def sort_desc(student: Student):
#             return -student.av_grade
#
#         nl = '\n'
#         result = []
#         for student in sorted(self.filtered, key=sort_desc):
#             result.append(f'{student.name} -> {student.av_grade:.2f}')
#         return nl.join(result)
#
#
# THRESHOLD = 4.50
# a = Academy()
# n = int(input())
#
# for _ in range(n):
#     name = input()
#     grade = float(input())
#     a.enroll(name, grade)
#
# a.filter(THRESHOLD)
# print(a)