def hourglassSum(arr):
    # Write your code here
    hourglass_coords = [(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)]  
    max_sum = -float('inf')

    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) -2):
            current_sum = 0
            for x, y in hourglass_coords:
                current_sum += arr[x + i][y + j]
            
            max_sum = max(max_sum, current_sum)
    return print(max_sum)

hourglassSum([
    [1 ,1 ,1 ,0 ,0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
])



# Here's the breakdown:

# 1. **`hourglass_coords`:** This is a list of coordinates representing the positions of an hourglass pattern within a 3x3 submatrix. Each tuple `(x, y)` represents the row and column offsets from the top-left corner of the submatrix.

# 2. **`max_sum`:** This variable is initialized to negative infinity (`-float('inf')`) to ensure that any valid sum in the array will be greater than this initial value.

# 3. **Nested Loops:**
#    - The outer loop (`for i in range(len(arr) - 2)`) iterates over the rows of the array, leaving space for a 3x3 submatrix.
#    - The inner loop (`for j in range(len(arr[i]) - 2)`) iterates over the columns of the array, leaving space for a 3x3 submatrix.

# 4. **Hourglass Sum Calculation:**
#    - Within the nested loops, there's another loop (`for x, y in hourglass_coords`) that iterates over the coordinates of the hourglass pattern.
#    - The coordinates are used to access the corresponding values in the 3x3 submatrix, and the sum of these values is calculated and stored in `current_sum`.

# 5. **Update Maximum Sum:**
#    - After calculating the sum for each hourglass pattern in the current 3x3 submatrix, the maximum of the current sum and the previous maximum (`max_sum`) is taken using `max(max_sum, current_sum)`.

# 6. **Print the Maximum Sum:**
#    - Finally, after the nested loops, the maximum sum is printed.

# This code is designed to find the maximum sum of hourglass patterns in a given 2D array. Each iteration of the nested loops corresponds to moving the 3x3 window across the array, calculating the sum of the hourglass pattern in each position, and updating the maximum sum accordingly.