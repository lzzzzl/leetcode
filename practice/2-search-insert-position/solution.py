from typing import List


class Solution1:
  """解法一: 左闭右闭
  """
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
      middle = left + (right - left) // 2
      if nums[middle] < target:
        left = middle + 1
      elif nums[middle] > target:
        right = middle - 1
      else:
        return middle
    
    return right + 1
  

class Solution2:
  """解法二: 左闭右开
  """
  def searchInsert(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums)

    while left < right:
      middle = left + (right - left) // 2
      if nums[middle] < target:
        left = middle + 1
      elif nums[middle] > target:
        right = middle
      else:
        return middle
      
    return left