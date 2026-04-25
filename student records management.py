import csv
import os
FILE_NAME = "students.csv"
FIELDNAMES = ["roll_no", "name", "age", "marks"]
def load_data():
    """Loads student data from the CSV file into a list of dictionaries."""
    students = []
    
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

def save_data(students):
    """Saves the list of dictionaries back to the CSV file."""
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student(students):
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ")
    
 
    for s in students:
        if s["roll_no"] == roll_no:
            print("Error: A student with this Roll Number already exists!")
            return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    marks = input("Enter Marks: ")
    
    new_student = {"roll_no": roll_no, "name": name, "age": age, "marks": marks}
    students.append(new_student)
    save_data(students)
    print(f"Student {name} added successfully!")

def view_students(students):
    print("\n--- Student Records ---")
    if not students:
        print("No records found.")
        return
    
    
    print(f"{'Roll No':<10} | {'Name':<15} | {'Age':<5} | {'Marks':<5}")
    print("-" * 45)
    
   
    for s in students:
        print(f"{s['roll_no']:<10} | {s['name']:<15} | {s['age']:<5} | {s['marks']:<5}")

def update_student(students):
    print("\n--- Update Student Marks ---")
    roll_no = input("Enter the Roll Number of the student to update: ")
    
    for s in students:
        if s["roll_no"] == roll_no:
            print(f"Current Marks for {s['name']}: {s['marks']}")
            new_marks = input("Enter New Marks: ")
            s["marks"] = new_marks
            save_data(students)
            print("Marks updated successfully!")
            return
            
    print("Student not found.")

def delete_student(students):
    print("\n--- Delete Student ---")
    roll_no = input("Enter the Roll Number of the student to delete: ")
    
    for i in range(len(students)):
        if students[i]["roll_no"] == roll_no:
            deleted_name = students[i]["name"]
            del students[i]
            save_data(students)
            print(f"Student {deleted_name} deleted successfully!")
            return
            
    print("Student not found.")

def main():
  
    students = load_data()
    
    while True:
        print("\n" + "="*30)
        print(" STUDENT MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Update Student Marks")
        print("4. Delete a Student")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("\nExiting program. Thanks and Have a Great Day !")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
