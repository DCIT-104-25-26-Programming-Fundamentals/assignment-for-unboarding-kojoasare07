def check_prime(value):
    if value < 2:
        return False
    for divisor in range(2, int(value ** 0.5) + 1):
        if value % divisor == 0:
            return False  
    return True 

if _name_ == "_main_":
    n = int(input("Enter a number: "))
    if check_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is NOT a prime number.")
