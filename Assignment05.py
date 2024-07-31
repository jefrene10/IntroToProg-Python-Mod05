# ------------------------------------------------------------------------------------------ #
# Title: Assignment 05
# Desc: Program displaying student's registration for a Python course.
#       Building Upon Assignment04, but adds use of dictionaries and exception handling
# Change Log: (Who, When, What)
#   EEnriquez, 07/29/2024, Created Script, Changed Option3 to support .json
#   EEnriquez, 07/30/2024, Tried to meet all requirements
# ------------------------------------------------------------------------------------------ #

import json

#Defining program constants
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
    """
FILE_NAME: str = "Enrollments.json"

#Defining program variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
json_data: str = ""
student_data: dict = [] # one row of student data
students: list = []  #table of students
csv_data: str = ""
file = None
menu_choice: str = ""


#When the program starts, read the file data
#Extract data from .json file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
#Incorporate exceptions
except FileNotFoundError as e:  #Error handling when the file is not found/doesn't exists
    print("The file could not be found!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')

except Exception as e:  #Error handling for non-specific error
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file.closed == False:
        file.close()

while True:
    # Present the menu to user
    print(MENU)
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

    #Get user input

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            # Get user input
            #student first name with error handling
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            # student last name with error handling
            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "Course": course_name}
        students.append(student_data)
        continue

    # Present the current data
    elif menu_choice == "2":
        print("\nThe current data is:")
        print("=" * 50)
        for student in students:
            print(f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["Course"]}")
        print("=" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            continue
        except TypeError as e:
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop

    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
