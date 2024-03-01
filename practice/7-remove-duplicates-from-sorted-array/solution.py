from typing import List


class Solution1:
    """解法一: 快慢指针法
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1


class Solution2:
    """解法二: 通用解法
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        def process(nums, k):
            idx = 0
            for x in nums:
                if idx < k or nums[idx - k] != x:
                    nums[idx] = x
                    idx += 1
            return idx
        return process(nums, 1)