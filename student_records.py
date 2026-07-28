def add_student(records):
    """Collects inputs to build a student dictionary and stores it in the records list."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))
    
    num_scores = int(input("How many scores? "))
    scores_list = []
    
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        if score.is_integer():
            score = int(score)
        scores_list.append(score)
        
    new_student = {
        "name": name,
        "id": student_id,
        "scores": scores_list
    }
    
    records.append(new_student)
    print(f'Student "{name}" added successfully.')

def display_all_students(records):
    """Prints a neatly formatted layout matrix table of all stored data logs."""
    if not records:
        print("No student records available.")
        return
        
    print("-" * 65)
    print(f"{'Name':<15} {'ID':<11} {'Scores':<18} {'Average':<7}")
    print("-" * 65)
    
    for student in records:
        scores_str = ", ".join(map(str, student["scores"]))
        
        if len(student["scores"]) > 0:
            avg_score = sum(student["scores"]) / len(student["scores"])
            avg_str = f"{avg_score:.2f}"
        else:
            avg_str = "0.00"
            
        print(f"{student['name']:<15} {student['id']:<11} {scores_str:<18} {avg_str:<7}")
        
    print("-" * 65)

def calculate_student_average(records):
    """Queries for a target ID value and outputs calculations if the record exists."""
    search_id = int(input("Enter student ID: "))
    
    for student in records:
        if student["id"] == search_id:
            if len(student["scores"]) > 0:
                avg_score = sum(student["scores"]) / len(student["scores"])
                print(f"{student['name']}'s average score: {avg_score:.2f}")
            else:
                print(f"{student['name']}'s average score: 0.00")
            return
            
    print("Error: Student ID not found.")

def display_menu():
    """Prints user choice interfaces block options template grid."""
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


if _name_ == "_main_":
    student_database = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_student(student_database)
        elif choice == "2":
            display_all_students(student_database)
        elif choice == "3":
            calculate_student_average(student_database)
        elif choice == "4":
            break
        else:
            print("Error: Invalid choice. Please pick an option from 1 to 4.")
