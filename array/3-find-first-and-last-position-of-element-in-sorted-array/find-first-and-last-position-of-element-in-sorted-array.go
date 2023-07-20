package main

type Solution1 struct{}

func (s Solution1) searchRange(nums []int, target int) []int {
	getRightBorder := func(nums []int, target int) int {
		left, right := 0, len(nums)-1
		rightBorder := -2
		for left <= right {
			middle := left + (right-left)/2
			if nums[middle] > target {
				right = middle - 1
			} else {
				left = middle + 1
				rightBorder = left
			}
		}
		return rightBorder
	}

	getLeftBorder := func(nums []int, target int) int {
		left, right := 0, len(nums)-1
		leftBorder := -2
		for left <= right {
			middle := left + (right-left)/2
			if nums[middle] >= target {
				right = middle - 1
				leftBorder = right
			} else {
				left = middle + 1
			}
		}
		return leftBorder
	}

	leftBorder := getLeftBorder(nums, target)
	rightBorder := getRightBorder(nums, target)

	if leftBorder == -2 || rightBorder == -2 {
		return []int{-1, -1}
	}
	if rightBorder-leftBorder > 1 {
		return []int{leftBorder + 1, rightBorder - 1}
	}
	return []int{-1, -1}
}
