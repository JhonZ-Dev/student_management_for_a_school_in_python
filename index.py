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

    def load_students(self):
        if os.path.exists(self.students_filename):
            with open(self.students_filename, 'rb') as file:
                return pickle.load(file)
        return []
    def save_students(self):
            with open(self.students_filename, 'wb') as file:
                pickle.dump(self.students, file)
    def add_student(self, student):
        self.students.append(student)
        self.save_students()
        print(f'Estudiante "{student.name}" añadido con éxito.')
    def assign_grade(self, student_id, subject, grade):
        for student in self.students:
            if student.student_id == student_id:
                student.grade[subject] = grade
                self.save_students()
                print(f'Calificación asignada a {student.name} en {subject}: {grade}.')
                return
        print(f'Estudiante con ID {student_id} no encontrado.')
    def generate_academic_report(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f'\n--- Informe Académico para {student.name} ---')
                if not student.grade:
                    print("Aún no se han asignado calificaciones.")
                else:
                    for subject, grade in student.grade.items():
                        print(f"{subject}: {grade}")
                return
        print(f'Estudiante con ID {student_id} no encontrado.')
def main():
    school_manager = SchoolManager()
    while True:
        print("\n--- Sistema de Gestión Escolar ---")
        print("1. Agregar estudiante")
        print("2. Asignar calificación")
        print("3. Generar informe académico")
        print("4. Salir")

        choice = input("Ingrese su elección (1-4): ")
        if choice == '1':
            student_id = input("Ingrese el ID del estudiante: ")
            student_name = input("Ingrese el nombre del estudiante: ")
            new_student = Student(student_id, student_name)
            school_manager.add_student(new_student)
        elif choice == '2':
            student_id = input("Ingrese el ID del estudiante: ")
            subject = input("Ingrese la materia: ")
            grade = float(input("Ingrese la calificación: "))
            school_manager.assign_grade(student_id, subject, grade)
        elif choice == '3':
            student_id = input("Ingrese el ID del estudiante para generar el informe académico: ")
            school_manager.generate_academic_report(student_id)
        elif choice == '4':
            school_manager.save_students()
            print("Saliendo del programa. ¡Hasta luego!")
            break
