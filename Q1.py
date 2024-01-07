class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Student(Person):
    def __init__(self, student_id, name, age, gender):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.courses_enrolled = {}

    def enroll_in_course(self, course):
        self.courses_enrolled[course.course_code] = course

    def calculate_gpa(self):
        # Implementation to calculate GPA based on grades in enrolled courses
        pass

class Professor(Person):
    def __init__(self, employee_id, name, age, gender):
        super().__init__(name, age, gender)
        self.employee_id = employee_id

    def grade_student(self, student, course, grade):
        # Implementation to assign grades to students
        pass

class Course:
    def __init__(self, course_code, course_name, professor):
        self.course_code = course_code
        self.course_name = course_name
        self.professor = professor
        self.students_enrolled = []

    def add_student(self, student):
        self.students_enrolled.append(student)

# Example usage:
professor1 = Professor(101, "Dr. Smith", 40, "Male")
student1 = Student(1001, "John Doe", 20, "Male")
student2 = Student(1002, "Jane Doe", 21, "Female")

course1 = Course("CS101", "Introduction to Computer Science", professor1)

professor1.grade_student(student1, course1, "A")
professor1.grade_student(student2, course1, "B")

student1.enroll_in_course(course1)
student2.enroll_in_course(course1)
