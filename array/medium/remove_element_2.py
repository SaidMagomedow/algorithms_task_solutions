# task - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    """
    RU:
    Алгоритм решения:
    - Изначально задаем k как 2, потому что первые два элемента могут быть как дублями, так и уникальными элементами
    - Начинаем итерацию так же с 2 индекса, по той же причине, что и выше
    """
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
