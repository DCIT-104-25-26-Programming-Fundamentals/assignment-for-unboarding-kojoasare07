def print_single_table(num):
    """
    Generates and prints a multiplication table for a specific number from 1 to 12.
    """
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num:<2} x  {i:<2} =  {num * i}")

def print_multiple_tables(n):
    """
    Generates full multiplication tables for every number from 1 up to N.
    Uses a separator line between each table.
    """
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        if current_num < n:
            print("-" * 27)


if _name_ == "_main_":
    print("--- PART A: Single Table ---")
    single_num = int(input("Enter a number: "))
    
    if single_num <= 0:
        print("Error: Value must be a positive integer.")
    else:
        print_single_table(single_num)
        
    print("\n--- PART B: Tables from 1 to N ---")
    max_range = int(input("Enter a number N: "))
    
    if max_range <= 0:
        print("Error: N must be a positive integer.")
    else:
        print_multiple_tables(max_range)
