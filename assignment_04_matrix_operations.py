# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR-CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# 

def read_matrix(rows, columns, matrix_name="Matrix"):
    matrix = []

    print(f"\nEnter values for {matrix_name}:")
    for members in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {members + 1}: ").split()))

            if len(row) != columns:
                print(f"Please enter exactly {columns} values.")
            else:
                matrix.append(row)
                break

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    transposed = []

    for i in range(columns):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        transposed.append(row)

    return transposed


def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    columns = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result


def main():
   

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, columns, "Matrix")

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix))


    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    matrix1 = read_matrix(rows, columns, "Matrix A")
    matrix2 = read_matrix(rows, columns, "Matrix B")

    print("\nResult of Addition:")
    print_matrix(add_matrices(matrix1, matrix2))


    rows_a = int(input("Enter rows for Matrix A: "))
    cols_a = int(input("Enter columns for Matrix A: "))

    matrix_a = read_matrix(rows_a, cols_a, "Matrix A")

    rows_b = int(input("Enter rows for Matrix B: "))
    cols_b = int(input("Enter columns for Matrix B: "))

    if cols_a != rows_b:
        print("\nMatrix multiplication is not possible.")
        print("Columns of Matrix A must equal rows of Matrix B.")
        return

    matrix_b = read_matrix(rows_b, cols_b, "Matrix B")

    print("\nResult of Multiplication:")
    print_matrix(multiply_matrices(matrix_a, matrix_b))


main()