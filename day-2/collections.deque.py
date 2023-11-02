# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

if __name__ == "__main__":
    n = int(input())
    d = deque()
    for i in range(n):
        z = input().split()
        if z[0] == 'append':
            d.append(int(z[1]))
        elif z[0] == 'pop':
            d.pop()
        elif z[0] == 'popleft':
            d.popleft()
        elif z[0] == 'appendleft':
            d.appendleft(int(z[1]))
    for z in d:
        print(z,end=" ")

# This Python code appears to be implementing a simple deque (double-ended queue) operation based on user input. It uses the `collections` module to import the `deque` data structure for efficient queue-like operations. Let's break down the code step by step:

# 1. `from collections import deque`: This line imports the `deque` data structure from the `collections` module.

# 2. `n = int(input())`: This line reads an integer `n` from the user, which represents the number of operations to be performed on the deque.

# 3. `d = deque()`: This line initializes an empty deque called `d`.

# 4. The code then enters a loop that will run `n` times, where each iteration performs one of the following operations based on user input:

#    - `z = input().split()`: This line reads a line of input from the user and splits it into a list of strings, where the first element (index 0) represents the operation to be performed, and the second element (if applicable) is the value to be operated on.

#    - The code uses a series of `if` and `elif` statements to check the first element of the `z` list (i.e., `z[0]`) to determine the operation to be performed:
#      - If `z[0]` is `'append'`, it appends the integer value `int(z[1])` to the right end of the deque using `d.append(int(z[1]))`.
#      - If `z[0]` is `'pop'`, it removes and discards the rightmost element from the deque using `d.pop()`.
#      - If `z[0]` is `'popleft'`, it removes and discards the leftmost element from the deque using `d.popleft()`.
#      - If `z[0]` is `'appendleft'`, it appends the integer value `int(z[1])` to the left end of the deque using `d.appendleft(int(z[1]))`.

# 5. After processing all the user input operations, the code enters another loop with `for z in d:` to iterate through the elements in the deque `d`.

# 6. Inside this loop, it prints each element in the deque with a space as the separator and without a newline character. This means the elements will be printed on the same line with spaces between them.

# In summary, this code takes user input to perform various operations on a deque and then prints the elements in the deque after all the operations are completed. The operations include appending elements to both ends of the deque, popping elements from the right end, and popping elements from the left end.