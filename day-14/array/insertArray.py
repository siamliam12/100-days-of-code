intArray = [0] * 6
length = 0
for i in range(0,3):
    intArray[length] = i
    length += 1

intArray[length] = 20
for i in range(3,-1,-1):
    intArray[i+1] =intArray[i]

for i in range(len(intArray)):
    print(f"Index {i} contains {intArray[i]}")