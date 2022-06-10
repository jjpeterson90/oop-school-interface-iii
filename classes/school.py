from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student
        return False

    def add_student(self, student_data):
        self.students.append(Student(student_data))
        pass
    
    def remove_student(self, school_id):
        if self.find_student_by_id(school_id) != False:
            student = self.find_student_by_id(school_id)
            self.students.remove(student)
            print(f"{student.name} deleted.")
            return
        print("Student not found")
        return
        