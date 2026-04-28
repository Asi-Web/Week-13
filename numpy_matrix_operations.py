## Asiwome Agbleze
## CMSC 111/1
## Assignment 1: Numpy Array and Matrix Operations

# numpy_matrix_operations.py

# This program demonstrates basic NumPy operations:
# 1. Create an array from 1 to 100
# 2. Reshape it into a 10 x 10 matrix
# 3. Extract rows 5 through 8 using zero-based indexing
# 4. Compute the sum of all elements

import numpy as np


def main():
    """Run the NumPy matrix operations assignment."""
    try:
        # Task 1: Create a NumPy array containing numbers 1 through 100
        numbers = np.arange(1, 101)

        print("Original Array:")
        print(numbers)
        print()

        # Task 2: Reshape the array into a 10 x 10 matrix
        matrix = numbers.reshape(10, 10)

        print("10 x 10 Matrix:")
        print(matrix)
        print()

        # Task 3: Extract rows 5 through 8
        # Zero-based indexing means:
        # row 5 is index 4
        # row 8 is index 7
        selected_rows = matrix[4:8]

        print("Rows 5 through 8:")
        print(selected_rows)
        print()

        # Task 4: Compute the sum of all elements in the matrix
        total_sum = np.sum(matrix)

        print("Sum of all elements:")
        print(total_sum)

    except ValueError as e:
        print("ValueError:", e)
        print("The array could not be reshaped as requested.")
    except Exception as e:
        print("An unexpected error occurred:", e)


# Run the program
if __name__ == "__main__":
    main()

