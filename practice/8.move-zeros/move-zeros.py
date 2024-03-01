from typing import List


class Solution1:
    """解法一: 双指针法
    """
    def moveZeroes(self, nums: List[int]) -> None:
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


class Solution3:
    """移动零到前面的位置
    """
    def moveZeroes(self, nums: List[int]) -> None:
        slow = len(nums) - 1
        for fast in range(len(nums) - 1, -1, -1):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow -= 1
