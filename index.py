import os
import pickle
class Student:
    def __init__(self, student_id, name, grade={}):
        self.student_id = student_id
        self.name = name
        self.grade = grade