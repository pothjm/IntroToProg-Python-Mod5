#---------------------------------------------------------------------------------------------------------------------#
# Title: Assignment05
# Desc: This assignment demonstrates working with dictionaries and exceptions
# Change Log: (Who, When, What)
# Jameson Poth, 8/13/2025, Created Script File
#---------------------------------------------------------------------------------------------------------------------#

import json

# This is a constant string representing the menu options the user has
MENU: str = ("---- Course Registration Program ----\n"
             "Select from the following menu:\n"
             "1. Register a Student for a Course\n"
             "2. Show current data\n"
             "3. Save data to a file\n"
             "4. Exit the program\n"
             "-----------------------------------------")
# The file name that data will be saved to
FILE_NAME: str = "Enrollments.json"

# This section assigns variables to an empty string
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
menu_choice: str = ""
# This sets the variable to data type None
file = None
# This section assigns variables to an empty list
student_data: dict[str,str] = {}
students: list = []

try:
    # This code opens a file, reads the data in it
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()

except FileNotFoundError as e:
    print('This file does not exist. Creating document and continuing..')
    file = open(FILE_NAME, "w")
except Exception as e:
    print("There was an error opening up the document")
    print(e,e.__doc__)

finally:
    file.close()

# Counter used in while loop
counter = 0

while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        try:
            # This is requesting the user to input the student's first name
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError('First name can only have alphabetic characters')
            # This is requesting the user to input the student's last name
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError('Last name can only have alphabetic characters')
            # This is requesting the user to input the course name
            course_name = input("Enter the course name: ")

            # Formatting the data to be a string separated by commas
            student_data = {'FirstName': student_first_name,\
            'LastName': student_last_name,'CourseName': course_name}
            students.append(student_data)
        except ValueError as e:
            print('User entered invalid information.\n',e)
            continue
        finally:
            counter = 0
            print("\n")
            continue

    elif menu_choice == "2":
        print("The current data is:")
        for row in students:
            print(f"{row["FirstName"]},{row["LastName"]},{row["CourseName"]}")
        counter = 0
        continue

    elif menu_choice == "3":
        try:
            # This code opens a file, writes the data to it, and closes it
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("The following data was written to the", \
                  FILE_NAME, "file:", student_data, "\n")
        except Exception as e:
                print('There was an error writing to the document ')
                print(e,e.__doc__)
        finally:
            file.close()

            counter = 0
            continue

    elif menu_choice == "4":

        break

    else:
        counter += 1
        if counter == 3:
            print("Too many incorrect inputs")
            break

        print("Please choose a choice from the menu by typing the \
corresponding numerical value \n")

        continue

print("Program Ended")