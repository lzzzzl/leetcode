class Solution1:
    """解法一: 二分查找法【左闭右闭】
    """
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 0, x
        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle <= x < (middle + 1) * (middle + 1):
                return middle
            elif x < middle * middle:
                right = middle - 1
            else:
                left = middle + 1
