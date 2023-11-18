# Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        currentCount = 0
        max_count = 0
        for num in nums:
            if num == 1:
                currentCount += 1
                max_count = max(max_count,currentCount)
            else:
                currentCount = 0
        return max_count
            

solution = Solution()
result = solution.findMaxConsecutiveOnes([1, 1,0,1,1,1,0,1,1,1,1,0,1])
print(result)