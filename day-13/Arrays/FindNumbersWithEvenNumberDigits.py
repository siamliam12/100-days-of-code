# Given an array nums of integers, return how many of them contain an even number of digits.
def countDigits(num):
    if num//10 == 0:
        return 1
    else:
        return 1+(countDigits(num//10))
    
class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        even = 0
        for i in range(len(nums)):
            if countDigits(nums[i]) %2 ==0:
                even +=1
        return even
    
solution = Solution()
result = solution.findNumbers([12,345,2,6,7896])
print(result)
