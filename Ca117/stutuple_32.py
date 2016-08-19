from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])

student1 = Student('Joe', 'Mannion', 98365338)
student2 = Student('Louise', 'Callaghan', 99324761)
student3 = Student(firstname='Noel', id=99071239, surname='Rooney')
stulist = [student1, student2, student3]

print (student1.firstname)
