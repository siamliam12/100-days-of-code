# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
def quickSort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num)//2]
    right = []
    left = []
    middle = []

    for i in num:
        if i < pivot:
            left.append(i)
        if i == pivot:
            middle.append(i)
        if i > pivot:
            right.append(i)
    return quickSort(left) + middle + quickSort(right)
class Solution:

    def findNumbers(self, nums: list[int]) -> int:
        squareList = []
        for num in nums:
            square = num * num
            squareList.append(square)
        answer = quickSort(squareList)
        print("[" + ",".join(map(str, answer)) + "]")
        # print(squareList)

solution = Solution()
result = solution.findNumbers([-4,-1,0,3,10])

