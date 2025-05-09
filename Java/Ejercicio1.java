// Median of Two Sorted Arrays
// Given two sorted arrays nums1 and nums2 of size m and n respectively,
// return the median of the two sorted arrays.

// Example 1:
// Input: nums1 = [1, 3], nums2 = [2]
// Output: 2.00000

// Example 2:
// Input: nums1 = [1, 2], nums2 = [3, 4]
// Output: 2.50000

import java.util.Arrays;

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int length1 = nums1.length;
        int length2 = nums2.length;
        int length3 = length1 + length2;

        int [] nums3 = new int[length3];

        for (int i = 0; i < length1; i++) {
            nums3[i] = nums1[i];
        }

        for (int i = 0; i < length2; i++){
            nums3[length1 + i] = nums2[i];
        }

        Arrays.sort(nums3);

        if (length3 % 2 == 0){
            int mid1 = length3 / 2 - 1;
            int mid2 = length3 / 2;
            return (nums3[mid1] + nums3[mid2]) / 2.0;
        } else {
            int mid = length3 / 2;
            return nums3[mid];
        }
    }
}