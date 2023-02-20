# Python Program to create a Student Management System
# display Student Details
def displayStudent(rollno):
    print("Roll Number: ", rollno["rollno"])
    print("Name: ", rollno["name"])
    print("Branch: ", rollno["branch"])
    print("Year: ", rollno["year"])


# search Student Details
def searchStudent(rollno, rollnoList):
    for student in rollnoList:
        if student["rollno"] == rollno:
            return student

    return 0


# Create Student Database
rollnoList = [{"rollno": 1, "name": "John", "branch": "CSE", "year": 2020},
              {"rollno": 2, "name": "Herry", "branch": "ECE", "year": 2020},
              {"rollno": 3, "name": "Mike", "branch": "EEE", "year": 2020}]


# Update Student Details
def updateStudent(rollno, rollnoList):
    search = searchStudent(rollno, rollnoList)
    if search != 0:
        search["name"] = input("Enter Updated Name: ")
        search["branch"] = input("Enter Updated Branch: ")
        search["year"] = input("Enter Updated Year: ")
    else:
        print("Roll Number not found")

    # Delete Student Details


def deleteStudent(rollno, rollnoList):
    search = searchStudent(rollno, rollnoList)
    if search != 0:
        rollnoList.remove(search)
    else:
        print("Roll Number not found")

    # Driver Code


if __name__ == '__main__':
    print("Student Management System")
    print("1. Display Student Details")
    print("2. Search Student Details")
    print("3. Update Student Details")
    print("4. Delete Student Details")
    print("5. Exit")

    while (1):
        choice = int(input("Enter your choice: "))

        if choice == 1:
            for student in rollnoList:
                displayStudent(student)
                print("")
        elif choice == 2:
            rollno = int(input("Enter Roll Number to search: "))
            student = searchStudent(rollno, rollnoList)
            if student != 0:
                displayStudent(student)
            else:
                print("Roll Number not found")
        elif choice == 3:
            rollno = int(input("Enter Roll Number to update: "))
            updateStudent(rollno, rollnoList)
        elif choice == 4:
            rollno = int(input("Enter Roll Number to delete: "))
            deleteStudent(rollno, rollnoList)
        elif choice == 5:
            break
        else:
            print("Invalid Choice")