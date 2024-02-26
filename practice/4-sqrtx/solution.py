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
    return -1
  

class Solution2:
    """解法二: 二分查找法【左闭右开】
    """
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 0, x + 1
        while left < right:
            middle = left + (right - left) // 2
            if middle * middle <= x < (middle + 1) * (middle + 1):
                return middle
            elif x < middle * middle:
                right = middle
            else:
                left = middle + 1
        return -1
     

class Solution3:
   """解法三: 牛顿迭代法
   """
   def mySqrt(self, x: int) -> int:
    if x <= 1:
        return x
    y = x // 2
    while y * y > x:
        y = (y + x // y) // 2
    return int(y)