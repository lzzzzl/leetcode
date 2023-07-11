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
    

class Solution2:
    """解法二: 二分查找法
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
        # nums 中 存在 target, 则左右滑动指针, 来找到符合题意的区间
        left, right = index, index
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]


class Solution3:
    """解法3
        1、首先，在 nums 数组中二分查找得到第一个大于等于 target的下标（左边界）与第一个大于target的下标（右边界）；
        2、如果左边界<= 右边界，则返回 [左边界, 右边界]。否则返回[-1, -1]
    """