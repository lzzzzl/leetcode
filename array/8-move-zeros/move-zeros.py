from typing import List


class Solution1:
    """解法一: 双指针法
    """
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


class Solution2:
    """解法二: 双指针变种方法
    """
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                j += 1
                continue
            i += 1
        for _ in range(j):
            nums.append(0)