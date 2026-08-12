import csv
# CSV file name
file_name = "student_grades.csv"
print("===== STUDENT GRADEBOOK =====")
while True:
    print("\n1. Add Student Record")
    print("2. View All Records")
    print("3. Exit")
    choice = input("Enter your choice: ")
    # ------------------------------------------------
    # Option 1: Add a student record
    # ------------------------------------------------
    if choice == "1":
        name = input("Enter student name: ").strip()
        subject = input("Enter subject name: ").strip()
        # Check empty information
        if name == "" or subject == "":
            print("Name and subject cannot be empty.")
            continue
        # Handle incorrect marks input
        try:
            marks = int(input("Enter marks from 0 to 100: "))
        except ValueError:
            print("Please enter marks as a number.")
            continue
        # Check marks range
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue
        # Calculate grade
        if marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"
        # Save record in the CSV file
        with open(file_name, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                name.title(),
                subject.title(),
                marks,
                grade
            ])
        print("Student record saved successfully.")
        print("Grade:", grade)
    # ------------------------------------------------
    # Option 2: View all saved records
    # ------------------------------------------------
    elif choice == "2":
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                record_found = False
                print("\n===== ALL STUDENT RECORDS =====")
                for row in reader:
                    record_found = True
                    print("\nName:", row[0])
                    print("Subject:", row[1])
                    print("Marks:", row[2])
                    print("Grade:", row[3])
                if record_found == False:
                    print("No records are available.")
        except FileNotFoundError:
            print("No gradebook file was found.")
            print("Please add a student record first.")
    # ------------------------------------------------
    # Option 3: Exit
    # ------------------------------------------------
    elif choice == "3":
        print("Student Gradebook closed.")
        break
    # Incorrect menu choice
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")