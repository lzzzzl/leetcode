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

type Solution2 struct{}

func (s Solution2) searchRange(nums []int, target int) []int {
	index := binarySearch(nums, target)
	if index == -1 {
		return []int{-1, -1}
	}
	left, right := index, index
	for left-1 >= 0 && nums[left-1] == target {
		left -= 1
	}
	for right+1 < len(nums) && nums[right+1] == target {
		right += 1
	}
	return []int{left, right}
}

func binarySearch(nums []int, target int) int {
	left, right := 0, len(nums)-1
	for left <= right {
		middle := left + (right-left)/2
		if nums[middle] > target {
			right = middle - 1
		} else if nums[middle] < target {
			left = middle + 1
		} else {
			return middle
		}
	}

	return -1
}

func main() {
	s := Solution1{}
	s.searchRange([]int{5, 7, 7, 8, 8, 10}, 8)
}
