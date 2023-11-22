def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+1)
    for a,b,k in queries:
        arr[a+1] += k
        arr[b] -= k

    max_sum = 0
    current_sum = 0
    for val in arr:
        current_sum += val
        max_sum = max(max_sum, current_sum)
    return max_sum
arrayManipulation(10,
                  [
                      [1,5,3],
                      [4,8,7],
                      [6,9,1],
                  ])