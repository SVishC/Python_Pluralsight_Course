students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase = student["name"].title()
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)



def add_student(name, student_id=121):
    student = {"name" : name, "student_id": student_id}
    students.append(student)


while input("Do you want to add user ?") == "yes":
    student_name = input("Enter the student name :")
    student_id = input("Enter the student name :")
    add_student(student_name, student_id)
    print_students_titlecase()



