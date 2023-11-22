def rotateLeft(d, arr):
    rotate = d % len(arr)
    rotateLeft = arr[rotate:] + arr[:rotate]
    print(rotateLeft)
rotateLeft(3,[5,1,2,3,4])