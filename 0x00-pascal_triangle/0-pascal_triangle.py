#!/usr/bin/python3

def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []  # Return an empty list if n is invalid
    containerArray = []  # Initialize the container array to store the triangle
    pascalArray = [1]  # Initialize the first row of the triangle with 1
    containerArray.append(pascalArray.copy())  # Append a copy of the first row to the container array

    # Handle the case when n is 1
    if n == 1:
        return [[1]]  # Return a list containing the first row if n is 1

    pascalArray.append(1)  # Add the second element (1) to the first row
    containerArray.append(pascalArray.copy())  # Append a copy of the updated first row to the container array

    triangle = []  # Initialize an empty list to store the current row of the triangle
    # Generate subsequent rows of the triangle
    for number in range(0, n - 2):
        originalArray = [1, 1]  # Initialize the current row with the first and last elements (1)
        # Calculate the values of the inner elements of the current row
        for index in range(0, len(pascalArray) - 1):
            # Calculate the sum of two adjacent elements from the previous row
            sum = pascalArray[index] + pascalArray[index + 1]
            # Insert the sum at the appropriate position in the current row
            originalArray.insert(index + 1, sum)
            triangle = originalArray.copy()  # Copy the current row to the triangle list
        pascalArray = triangle.copy()  # Update the previous row with the current row
        containerArray.append(pascalArray)  # Append the current row to the container array

    return containerArray  # Return the complete Pascal's triangle as a list of lists

