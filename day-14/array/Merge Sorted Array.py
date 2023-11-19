# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def quickSort(arr):
    if len(arr) == 1:return arr
    pivot = arr[len(arr)//2]
    middle=[]
    right = []
    left = []
    for i in arr:
        if i < pivot:
            left.append(i)
        if i == pivot:
            middle.append(i)   
        if i == pivot:
            right.append(i)
    return quickSort(left) + middle + quickSort(right)
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        for i in range(len(nums1)):
            if nums1[i] == 0:
                pass
            else:
                merged.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] == 0:
                pass
            else:
                merged.append(nums2[j])
        print(quickSort(merged))

solution =Solution()
solution.merge([1,2,3,0,0,0],3,[2,5,6],3)