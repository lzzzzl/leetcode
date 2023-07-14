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


class Solution2:
    """解法二: 二分查找法【左闭右开】
    """

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 0, x + 1
        while left < right:
            middle = left + (right - left) // 2
            if middle * middle <= x < (middle+1) * (middle+1):
                return middle
            elif x < middle * middle:
                right = middle
            else:
                left = middle + 1


class Solution3:
    """解法三: 牛顿迭代法

    牛顿迭代法是一种求解无约束优化问题的方法，基于泰勒级数展开以及牛顿-莱布尼茨公式。在求解平方根的问题上，它可以被用来找到满足 f(y) = y^2 - x = 0 的 y 值。

    牛顿迭代法的基本思想是，首先猜测一个值 y，并不断更新这个猜测值，直到找到一个 y 使得 f(y) 足够接近 0。更新猜测值的公式如下：

        y_new = y - f(y) / f'(y)

    其中 f'(y) 是 f(y) 对 y 的导数。在这个问题中，f(y) = y^2 - x，因此 f'(y) = 2y。将这些代入更新公式中，我们可以得到：

        y_new = y - (y^2 - x) / 2y
        = y/2 + x / (2y)
        = (y + x / y) / 2

        这就是我们在代码中使用的公式 y = (y + x / y) // 2。

    公式 y_new = y - f(y) / f'(y) 的意思是：新的猜测值 y_new 是当前猜测值 y 减去 f(y) 与 f'(y) 的比值。

    在这个公式中：

        y 是当前的猜测值
        f(y) 是方程 f 在 y 处的值
        f'(y) 是方程 f 在 y 处的导数值

        这个公式来源于泰勒级数的一阶近似。它利用了方程在当前猜测值附近的局部线性性质，来更新当前猜测值，使得新的猜测值更接近方程的根。
    """

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        y = x // 2
        while y * y > x:
            y = (y + x / y) // 2
        return int(y)
