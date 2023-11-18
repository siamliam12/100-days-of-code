squareNumbers = [0]*10

for i in range(10):
    square = (i+1)* (i+1)
    squareNumbers[i] = square

    print(squareNumbers[i])
print('---------------------------------------------------------------')
for square in squareNumbers:
    print(square)