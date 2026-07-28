def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return round(a / b, 2)

def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a % b

def exponentiate(a, b):
    return a ** b

def display_menu():
    print("\n============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

if _name_ == "_main_":
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")
        
        if choice == "7":
            print("Goodbye!")
            break
            
        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter first number : "))
                num2 = float(input("Enter second number: "))
                
                if num1.is_integer(): num1 = int(num1)
                if num2.is_integer(): num2 = int(num2)
                
                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    res = divide(num1, num2)
                    if isinstance(res, str):  
                        print(res)
                    else:
                        print(f"Result: {num1} / {num2} = {res}")
                elif choice == "5":
                    res = modulus(num1, num2)
                    if isinstance(res, str):
                        print(res)
                    else:
                        print(f"Result: {num1} % {num2} = {res}")
                elif choice == "6":
                    print(f"Result: {num1} ** {num2} = {exponentiate(num1, num2)}")
                    
            except ValueError:
                print("Error: Invalid numeric input. Please enter valid numbers.")
        else:
            print("Error: Invalid selection. Please pick a number from 1 to 7.")
