from typing import List


class Solution1:
    """解法一: 从头到尾遍历数组，每遇到一个等于 val 的元素，
              就将该元素与数组的最后一个元素交换，然后数组的长度减 1
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n


class Solution2:
    """解法二: 双指针
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
    

class Solution3:
    """解法三: 双指针的另一种写法
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
        