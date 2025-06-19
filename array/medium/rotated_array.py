# task -

class Solution:

    @staticmethod
    def rotate(nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        rotated = [0] * n

        for i in range(n):
            c = (i + k) % n
            rotated[c] = nums[i]

        for i in range(n):
            nums[i] = rotated[i]

Solution.rotate(nums=[1,2,3,4,5,6], k=2)