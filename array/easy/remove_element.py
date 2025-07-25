# task - https://leetcode.com/problems/remove-element/?envType=problem-list-v2&envId=array
from typing import List


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
