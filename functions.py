students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)



def add_student(name, student_id=121):
    student = {"name" : name, "student_id": student_id}
    students.append(student)


def save_file(student_name): #Save student name to file
    try:
        f=open("students.txt","a")
        f.write(student_name+"\n") #adding new line because,we will read it later line by line(readlines())
        f.close()
    except Exception:
        print("Couldnot read the file")


def read_file(): #reads the file and add the value to students calling add_student() method
    try:
        f=open("students.txt","r")
        for student in f.readlines():
            add_student(student) #Here we are adding only student name but not id,
            # bcz to add id we have to process Dictionaries,which needs some importing of Pickle module
        f.close()
    except Exception:
        print("Couldn't read the file")

read_file()
print_students_titlecase()

student_name = input("Enter the student name :")
student_id = input("Enter the student id :")
add_student(student_name, student_id)
save_file(student_name)



