# Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

# Example 1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000

# Example 2:
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1 + nums2
        length = len(nums3)
        nums3.sort()

        if length % 2 == 0:
            index1 = length // 2 - 1
            index2 = length // 2
            return (nums3[index1] + nums3[index2]) / 2
        else:
            return nums3[length//2]