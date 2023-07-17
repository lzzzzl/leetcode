class Solution1:
    """解法一: 二分法
    """
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 0, num - 1
        while left <= right:
            middle = left + (right - left) // 2
            if middle * middle > num:
                right = middle - 1
            elif middle * middle < num:
                left = middle + 1
            else:
                return True
        return False


class Solution2:
    """解法二: 牛顿迭代法
    """
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        
        return x * x == num
