if __name__ == '__main__':
    n = 5
    # arr = [2, 3, 6 ,6, 5]
    arr =[1 ,-1, -2 ,-1]
    # arr =[-7, -7 ,-7, -7, -6]
    myset = set()
    duplicate = []
    for item in arr:
        if item in myset:
            duplicate.append(item)
        else:
            myset.add(item)
    myArray = list(myset)
    for num in myArray:
        for i in range(len(myArray)-1):
            if num > 0:
                if myArray[i] >= myArray[i + 1]:
                    myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]
            if num < 0:
                if myArray[i] >= myArray[i + 1]:
                    myArray[i], myArray[i + 1] = myArray[i + 1], myArray[i]
    if num > 0:
        print(myArray[-2])
    if num < 0:
        print(myArray[0])