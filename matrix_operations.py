def read_matrix(num_rows, num_cols):
    grid = []
    for r in range(num_rows):
        line = list(map(int, input(f"Enter row {r + 1}: ").split()))
        grid.append(line)
    return grid


def display_matrix(grid):
    pad = 0
    for line in grid:
        for entry in line:
            pad = max(pad, len(str(entry)))
    
    for line in grid:
        print("  ".join(str(entry).rjust(pad) for entry in line))


def transpose(grid):
    r_count = len(grid)          
    c_count = len(grid[0])       
  
    output = []
    for c in range(c_count):
        fresh_row = []
        for r in range(r_count):
            fresh_row.append(grid[r][c])   
        output.append(fresh_row)
    return output


def add_matrices(x, y):
    r_count = len(x)
    c_count = len(x[0])
    output = []
    for r in range(r_count):
        fresh_row = []
        for c in range(c_count):
            fresh_row.append(x[r][c] + y[r][c])   
        output.append(fresh_row)
    return output


def multiply_matrices(x, y):
    rows_x = len(x)          
    inner = len(x[0])        
    cols_y = len(y[0])       
    output = []
    for r in range(rows_x):
        fresh_row = []
        for c in range(cols_y):
            acc = 0
            for k in range(inner):
                acc += x[r][k] * y[k][c]
            fresh_row.append(acc)
        output.append(fresh_row)
    return output


def main():
    print("=== Part A: Transpose ===")
    num_rows = int(input("Enter number of rows: "))
    num_cols = int(input("Enter number of columns: "))
    grid = read_matrix(num_rows, num_cols)

    print("\nOriginal Matrix:")
    display_matrix(grid)
    print("\nTransposed Matrix:")
    display_matrix(transpose(grid))


    print("\n=== Part B: Addition ===")
    num_rows = int(input("Enter number of rows: "))
    num_cols = int(input("Enter number of columns: "))
    print("Matrix A:")
    x = read_matrix(num_rows, num_cols)
    print("Matrix B:")
    y = read_matrix(num_rows, num_cols)

    print("\nSum (A + B):")
    display_matrix(add_matrices(x, y))

 
    print("\n=== Part C: Multiplication ===")
    m = int(input("Enter rows of A (M): "))
    n = int(input("Enter columns of A / rows of B (N): "))
    p = int(input("Enter columns of B (P): "))
    print(f"Matrix A ({m}x{n}):")
    x = read_matrix(m, n)
    print(f"Matrix B ({n}x{p}):")
    y = read_matrix(n, p)

    print("\nProduct (A x B):")
    display_matrix(multiply_matrices(x, y))


if _name_ == "_main_":
    main()
