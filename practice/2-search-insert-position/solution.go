package main

import "fmt"

type Solution1 struct{}

func (s Solution1) searchInsert(nums []int, target int) int {
	left, right := 0, len(nums)-1

	for left <= right {
		middle := (left + right) / 2
		if nums[middle] < target {
			left = middle + 1
		} else if nums[middle] > target {
			right = middle - 1
		} else {
			return middle
		}
	}

	return right + 1
}

type Solution2 struct{}

func (s Solution2) searchInsert(nums []int, target int) int {
	left, right := 0, len(nums)

	for left < right {
		middle := (left + right) / 2
		if nums[middle] < target {
			left = middle + 1
		} else if nums[middle] > target {
			right = middle
		} else {
			return middle
		}
	}

	return left
}

func main() {
	s1 := Solution1{}
	sr := s1.searchInsert([]int{1, 3, 5, 6}, 5)
	fmt.Println(sr)

	s2 := Solution2{}
	sc := s2.searchInsert([]int{1, 3, 5, 6}, 5)
	fmt.Println(sc)
}
