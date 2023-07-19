from types import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] ** 2 > nums[j] ** 2:
                res[pos] = nums[i] ** 2
                i += 1
            else:
                res[pos] = nums[j] ** 2
                j -= 1
            pos -= 1
        return res
