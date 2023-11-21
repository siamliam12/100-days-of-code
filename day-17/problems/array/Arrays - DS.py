def reverseArray(a):
    # Write your code here
    left = 0
    right = len(a) -1 

    while left < right:
        temp = a[left]
        a[left] = a[right]
        a[right] = temp
        left += 1 
        right -= 1 
    return print(a)

reverseArray([1,4, 3, 2])
