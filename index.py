import os
import pickle
class Student:
    def __init__(self, student_id, name, grade={}):
        self.student_id = student_id
        self.name = name
        self.grade = grade
class SchoolManager:
    def __init__(self, students_filename="students.pkl"):
        self.students_filename = students_filename
        self.students = self.load_students()