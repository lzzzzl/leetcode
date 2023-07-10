from types import List

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
        # 情况一: target 在数组范围的右边或者左边，例如数组{3, 4, 5}，
        # target 为 2 或者数组 {3, 4, 5}, target 为 6，此时应该返回 
        # {-1, -1}
        if leftBorder == -2 or rightBorder == -2:
            return [-1, -1]
        # 情况三: target 在数组范围中，且数组中存在target，
        # 例如数组{3,6,7},target为6，此时应该返回{1, 1}
        if rightBorder - leftBorder > 1:
            return [leftBorder + 1, rightBorder - 1]
        # 情况二: target 在数组范围中，且数组中不存在target，
        # 例如数组{3,6,7},target为5，此时应该返回{-1, -1}
        return [-1, -1]