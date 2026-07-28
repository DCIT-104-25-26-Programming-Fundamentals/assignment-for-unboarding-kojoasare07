def calculate_sum(items):
    running_total = 0
    for element in items:
        running_total += element
    return running_total
  
def calculate_average(items):
    return calculate_sum(items) / len(items)
  
def find_maximum(items):
    highest = items[0]
    for element in items:
        if element > highest:
            highest = element
    return highest

def find_minimum(items):
    lowest = items[0]
    for element in items:
        if element < lowest:
            lowest = element
    return lowest

def main():
    count = int(input("How many numbers? "))
    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    items = []
    for idx in range(count):
        element = int(input(f"Enter number {idx + 1}: "))
        items.append(element)

    print("\nResults:")
    print(f"Sum:     {calculate_sum(items)}")
    print(f"Average: {calculate_average(items)}")
    print(f"Maximum: {find_maximum(items)}")
    print(f"Minimum: {find_minimum(items)}")

if _name_ == "_main_":
    main()
