package main

import "fmt"

type Solution1 struct{}

// Solution1: 左闭右闭区间
func (s Solution1) search(nums []int, target int) int {
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

	return -1
}

type Solution2 struct{}

// Solution2: 左闭右开区间
func (s Solution2) search(nums []int, target int) int {
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

	return -1
}

func main() {
	s1 := Solution1{}
	sr := s1.search([]int{-1, 0, 3, 5, 9, 12}, 9)
	fmt.Println(sr)

	s2 := Solution2{}
	sc := s2.search([]int{-1, 0, 3, 5, 9, 12}, 9)
	fmt.Println(sc)
}
