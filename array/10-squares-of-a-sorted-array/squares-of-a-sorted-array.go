package main

import "sort"

type Solution1 struct{}

func (s1 Solution1) sortedSquares(nums []int) []int {
	n := len(nums)
	res := make([]int, n)
	i, j, pos := 0, n-1, n-1
	for i <= j {
		if nums[i]*nums[i] > nums[j]*nums[j] {
			res[pos] = nums[i] * nums[i]
			i++
		} else {
			res[pos] = nums[j] * nums[j]
			j--
		}
		pos--
	}
	return res
}

type Solution2 struct{}

func (s2 Solution2) sortedSquares(nums []int) []int {
	for i := range nums {
		nums[i] = nums[i] * nums[i]
	}
	sort.Ints(nums)
	return nums
}
