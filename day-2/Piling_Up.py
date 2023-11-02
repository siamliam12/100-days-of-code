# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    T = int(input())
    
    for _ in range(T):
        block_size = int(input())
        block =list(map(int,input().split()))
        check = max(block[0],block[-1])
        yes_check = 0
        
        for _ in range(len(block)):
            if (block[0] >= block[-1]) and (check >= block[0]):
                check = block[0]
                block.pop(0)
                yes_check += 1
            elif (block[0] <= block[-1]) and (check >=block[-1]):
                check = block[-1]
                block.pop(-1)
                yes_check += 1
            else:
                print("No")
                break
        if yes_check == block_size:
            print("Yes")

# In the code snippet you provided, `block[0]` and `block[-1]` refer to elements of the `block` list, which is a list of block sizes. Here's what each of these expressions means:

# 1. `block[0]`: This refers to the first element of the `block` list. In Python, lists are zero-indexed, so `block[0]` accesses the element at the beginning of the list.

# 2. `block[-1]`: This refers to the last element of the `block` list. In Python, you can use negative indices to access elements from the end of the list, and `-1` represents the last element, `-2` would represent the second-to-last element, and so on.

# So, in the context of your code, `block[0]` represents the size of the leftmost cube, and `block[-1]` represents the size of the rightmost cube in the list of block sizes. The code calculates the maximum of these two values to determine the maximum block size at either end of the list.

# In the code snippet you provided, `check` is a variable that stores the result of calculating the maximum block size at either end of the list. The code calculates this maximum as:

# ```python
# check = max(block[0], block[-1])
# ```

# Here's what it does:

# - `block[0]` represents the size of the leftmost cube in the list of block sizes.
# - `block[-1]` represents the size of the rightmost cube in the list of block sizes.

# The `max()` function is used to determine the maximum value between these two values (i.e., the maximum size at either end). The result is then stored in the `check` variable.

# `check` is a single value that represents the maximum size among the two end blocks, and it can be used for further calculations or comparisons in your code.

# The code you've provided is part of a larger logic that checks whether it's possible to stack the cubes in the required order based on the rules provided. Let's break down the logic step by step:

# - `if (block[0] >= block[-1]) and (check >= block[0])`: This condition checks two things:
#   1. It checks whether the size of the leftmost cube (`block[0]`) is greater than or equal to the size of the rightmost cube (`block[-1]`).
#   2. It checks whether the maximum block size (`check`) is greater than or equal to the size of the leftmost cube (`block[0]`).

#   If both conditions are met, it means you can choose the leftmost cube and add it to the stack. In this case, you update `check` to be the size of the leftmost cube (`check = block[0]`), remove the leftmost cube from the list (`block.pop(0)`), and increment the `yes_check` variable (which likely keeps track of how many cubes you've successfully added to the stack).

# - `elif (block[0] <= block[-1]) and (check >= block[-1])`: This condition is similar to the previous one, but it checks the opposite scenario:
#   1. It checks whether the size of the leftmost cube (`block[0]`) is less than or equal to the size of the rightmost cube (`block[-1]`).
#   2. It checks whether the maximum block size (`check`) is greater than or equal to the size of the rightmost cube (`block[-1]`).

#   If both conditions are met, it means you can choose the rightmost cube and add it to the stack. In this case, you update `check` to be the size of the rightmost cube (`check = block[-1]`), remove the rightmost cube from the list (`block.pop(-1)`), and increment the `yes_check` variable.

# The purpose of this code is to simulate the process of selecting cubes from either the left or right end based on the rules of stacking. If the conditions are met, you add cubes to the stack, update the maximum block size (`check`), and keep track of the number of cubes successfully added (`yes_check`).

# This process continues until it's no longer possible to add cubes based on the given conditions, at which point you'll exit the loop and can determine whether it's possible to stack the cubes in the required order.

# Popping elements from the list is a key part of the algorithm because it simulates the process of selecting a cube and placing it on top of the stack while ensuring that you adhere to the stacking rules.

# In the context of this problem, the algorithm needs to determine if it's possible to stack the cubes in the required order, and it can only pick either the leftmost or the rightmost cube each time, depending on the conditions:

# - If the size of the leftmost cube (`block[0]`) is greater than or equal to the size of the rightmost cube (`block[-1]`), and the maximum block size (`check`) allows for the placement of the leftmost cube, it makes sense to pick and place the leftmost cube on top of the stack. By popping the leftmost cube from the list (`block.pop(0)`), you effectively remove it from consideration and simulate placing it on the stack.

# - Conversely, if the size of the leftmost cube (`block[0]`) is less than or equal to the size of the rightmost cube (`block[-1]`), and the maximum block size (`check`) allows for the placement of the rightmost cube, it makes sense to pick and place the rightmost cube on top of the stack. By popping the rightmost cube from the list (`block.pop(-1)`), you effectively remove it from consideration and simulate placing it on the stack.

# In both cases, the cubes are removed from consideration after being placed on the stack, and the `check` variable is updated to reflect the size of the cube that was just added to the stack. This process continues until it's no longer possible to add cubes based on the given conditions or until you've processed all the cubes.

# The goal is to simulate the stacking process, ensuring that you only pick cubes that can be legally placed on top of the stack while following the rules of the problem.