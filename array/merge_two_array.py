# tasks - https://leetcode.com/problems/merge-sorted-array/description/
from typing import List

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        l_n1_i = m - 1
        l_n2_i = n - 1
        l_s_i = m + n - 1

        while l_n1_i >= 0 and l_n2_i >= 0:
            if nums1[l_n1_i] < nums2[l_n2_i]:
                nums1[l_s_i] = nums2[l_n2_i]
                l_n2_i -= 1
            else:
                nums1[l_s_i] = nums1[l_n1_i]
                l_n1_i -= 1
            l_s_i -= 1

        while l_n2_i >= 0:
            nums1[l_s_i] = nums2[l_n2_i]
            l_n2_i -= 1
            l_s_i -= 1

