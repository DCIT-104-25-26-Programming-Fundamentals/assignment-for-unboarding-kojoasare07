def generate_fibonacci(count):
    result = []
    prev, curr = 0, 1
    for _ in range(count):
        result.append(prev)
        prev, curr = curr, prev + curr  
    return result

def is_fibonacci(target):
    if target < 0:
        return False
    prev, curr = 0, 1
    while prev < target:
        prev, curr = curr, prev + curr
    return prev == target

def main():
    count = int(input("How many terms? "))
    if count <= 0:
        print("Error: N must be a positive integer.")
    else:
        result = generate_fibonacci(count)
        print("Fibonacci sequence:", " ".join(str(term) for term in result))

   
    target = int(input("\nEnter a number to check: "))
    if is_fibonacci(target):
        print(f"{target} is a Fibonacci number.")
    else:
        print(f"{target} is NOT a Fibonacci number.")

if _name_ == "_main_":
    main()
