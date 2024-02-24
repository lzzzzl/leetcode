from typing import List


class Solution1:
    """解法一: 左闭右闭
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def getRightBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            rightBorder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
                    rightBorder = left

            return rightBorder

        def getLeftBorder(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            leftBorder = -2
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle - 1
                    leftBorder = right
                else:
                    left = middle + 1
            return leftBorder
        
        leftBorder = getLeftBorder(nums, target)
        rightBorder = getRightBorder(nums, target)

        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        
        if rightBorder - leftBorder > 1:
            return [leftBorder + 1, rightBorder - 1]

        return [-1, -1]
    

class Solution2:
    """解法二：二分查找法
    """
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            while left <= right:
                middle = left + (right - left) // 2
                if nums[middle] > target:
                    right = middle - 1
                elif nums[middle] < target:
                    left = middle + 1
                else:
                    return middle
            return -1
        index = binarySearch(nums, target)
        if index == -1:
            return [-1, -1]
        left, right = index, index
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]
