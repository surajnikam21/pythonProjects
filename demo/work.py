def student():
    student = {}
    student["Name"] = input("Name: ")
    student["Age"] = input("Age: ")
    student["Course"] = input("Course: ")
    student["City"] = input("City: ")
    print(type(student))
    return student


#students = student()
# with open('students.txt', 'a') as f:
#     f.write(students.__str__() + "\n")

# with open('students.txt', 'r') as f:
#     print(f.read())


choice = input('Do you want to enter student record(yes/no:)')

while(choice == 'yes'):
    students = student()
    with open('students.txt', 'a') as f:
        f.write(students.__str__() + "\n")
    choice = input('Do you want to enter another student record(yes/no:)')

print('Thank you')

with open('students.txt', 'r') as f:
    print(f.read())
