import os            # the os module is used to perform file-related operations, such as creating, renaming, deleting, and moving files.

# Function to generate degree in bulk
def myDegreeGenerator():
    # Open degreeData.txt file
    with open('degreeData.txt', 'r') as f:

        # Read the first line to get the number of data available in the text file
        num_degrees = int(f.readline().strip())
        # Loop through the remaining lines and generate degree for each student
        for i in range(num_degrees):
            data = ((f.readline()).strip()).split(',')
            name, roll_no, course, year, percentage = data
            date_of_issue=input(f"enter date of issue of the Degree for the student name {name} roll No: {roll_no}:")
            # Open degreeTemplate.txt file and replace placeholders with student's data
            with open('degreeTemplate.txt', 'r') as temp:
                degree = (temp.read()).format(Student_Name = name, Roll_number=roll_no, Name_of_Programme=course, Year=year,Percentage= percentage,date_of_creation=date_of_issue)
                # Save the degree in a text file with student's name and roll number
                with open(f'{name}_{roll_no}.txt', 'w') as file:
                    file.write(degree)
            print(f"Degree generated successfully for {name} ({roll_no})")

# Function to correct degree
def myDegreeCorrector():
    # Get the filename of the degree to be corrected
    filename = input('Enter the filename of the degree to be corrected: ')
    # Check if the file exists
    if not os.path.exists(filename):
        print('File not found!')
        return
    # Open the file and display the current contents
    with open(filename, 'r') as f:
        degree = f.read()
        print('Current content:\n' + degree)
        # Ask the user to make corrections
        while True:
            print("What correction would you like to make?")
            print("1. Name")
            print("2. Roll Number")
            print("3. Course Name")
            print("4. Year of Award")
            print("5. Percentage")
            print("6. Exit Correction")

            try:
                choice = int(input("Enter your choice(1/2/3/4/5/6): "))
                if choice == 1:
                    new_name = input("Enter new name: ")
                    degree = degree.replace(degree.split('\n')[0], f"Name: {new_name}")
                elif choice == 2:
                    new_roll_number = input("Enter new roll number: ")
                    degree = degree.replace(degree.split('\n')[1], f"Roll Number: {new_roll_number}")
                elif choice == 3:
                    new_course_name = input("Enter new course name: ")
                    degree = degree.replace(degree.split('\n')[2], f"Course Name: {new_course_name}")
                elif choice == 4:
                    new_year_of_award = input("Enter new year of award: ")
                    degree = degree.replace(degree.split('\n')[3], f"Year of Award: {new_year_of_award}")
                elif choice == 5:
                    new_percentage = input("Enter new percentage: ")
                    degree = degree.replace(degree.split('\n')[4], f"Percentage: {new_percentage}")
                elif choice == 6:
                    with open(filename, 'w') as degree_file:
                        degree_file.write(degree)
                    print("Degree corrected successfully!")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")



# Function to view degree
def myDegreeViewer():
    # Get the filename of the degree to be viewed
    filename = input('Enter the filename of the degree to be viewed: ')
    # Check if the file exists
    if not os.path.exists(filename):
        print('File not found!')
        return
    # Open the file and display the contents
    with open(filename, 'r') as f:
        degree = f.read()
        print(degree)

# Display menu
while True:
    print("Welcome to My Degree Generator!")
    print("Please select an option:")
    print('1. Generate degrees in bulk')
    print('2. Correct a degree')
    print('3. View a degree')
    print('4. Exit')
    option = input('Enter your option (1/2/3/4): ')
    if option == '1':
        myDegreeGenerator()
    elif option == '2':
        myDegreeCorrector()
    elif option == '3':
        myDegreeViewer()
    elif option == '4':
        print('Exiting...  "Thank you for using My Degree Generator!"')
        break
    else:
        print('Invalid option. Please enter 1, 2, 3 or 4.')
