# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        n = len(arr)
        for i in range(n-1,-1,-1):
            if i+zeros < n:
                arr[i+zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i+zeros < n:
                    arr[i+zeros] = 0
        print(arr)
solution = Solution()
result = solution.duplicateZeros([1,0,2,3,0,4,5,0])
