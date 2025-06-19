# task - https://leetcode.com/problems/majority-element/?envType=study-plan-v2&envId=top-interview-150

from typing import List
from collections import Counter


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:
        c = Counter(nums)
        res, _ = c.most_common(1)[0]
        return res
