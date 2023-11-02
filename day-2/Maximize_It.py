from itertools import product

K,M = map(int,input().split())

matrix = [list(map(int,input().split()[1:])) for i in range(K)]

combinations = list(product(*matrix))

print(max(sum(n*n for n in c) % M for c in combinations))

# 1. `from itertools import product`: This line imports the `product` function from the `itertools` module. The `product` function computes the Cartesian product of input iterables, which is essentially all possible combinations of elements from these input iterables.

# 2. `K, M = map(int, input().split())`: This line reads a line of input from the user. The input is expected to contain two integers separated by a space. These integers are assigned to the variables `K` and `M`. `K` and `M` are used to store the number of lists and a modulo value, respectively.

# 3. `matrix = [list(map(int, input().split()[1:])) for _ in range(K)]`: This is a list comprehension that reads `K` lines of input. For each line, it splits the input into space-separated values and converts them to integers. However, it discards the first value (index 0) from each line using `[1:]`. These values are then stored as lists in the `matrix` list.

# 4. `combinations = list(product(*matrix))`: This line uses the `product` function from the `itertools` module to calculate all possible combinations of elements from the `matrix` lists. The `*matrix` syntax is used to unpack the lists in the `matrix` list as separate arguments to the `product` function. The result is a list of tuples, where each tuple represents a combination of elements from the input lists.

# 5. `print(max(sum(n*n for n in c) % M for c in combinations))`: This line is where the main computation happens. It calculates the maximum value obtained by summing the squares of elements in each combination and then taking the result modulo `M`. Here's how it works:

#    - `for c in combinations`: It iterates over each combination (a tuple) in the `combinations` list.
#    - `sum(n*n for n in c)`: For each combination `c`, it calculates the sum of the squares of its elements.
#    - `% M`: It takes the modulo of the sum with the value of `M`.
#    - `max(...)`: It finds the maximum value among all the results obtained for different combinations.

# Finally, the maximum result is printed to the console.

# In summary, this code takes user input, generates combinations of elements from different input lists, calculates the maximum value obtained by summing the squares of these combinations and applying modulo `M`, and then prints the maximum result.