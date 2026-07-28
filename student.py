def get_grade(mark):
    if mark < 0 or mark > 100:
        return None
    if mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"
def main():
    student_mark = int(input("Enter student score (0-100): "))
    letter = get_grade(student_mark)
    if letter is None:
        print("Error: Score must be between 0 and 100.")
    else:
        print(f"Grade: {letter}")
if _name_ == "_main_":
    main()
