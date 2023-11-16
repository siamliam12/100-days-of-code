# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        sortedList = sorted(nums)
        sortedSet = set()
        for i in range(len(sortedList)):
            sortedSet.add(sortedList[i])
        k = len(sortedSet)
        temp = []
        for j in sortedSet:
            temp.append(j)
        nums = temp
        print(k)
        print(nums)

Solution = Solution()
Solution.removeDuplicates([1,3,5,8,2,5,9,0])