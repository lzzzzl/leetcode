package main

type Solution1 struct{}

func (s Solution1) removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	slow := 0
	for fast := 1; fast < len(nums); fast++ {
		if nums[fast] != nums[slow] {
			slow += 1
			nums[slow] = nums[fast]
		}
	}
	return slow + 1
}

type Solution2 struct{}

func (s Solution2) removeDuplicates(nums []int) int {
	return process(nums, 1)
}

func process(nums []int, k int) int {
	idx := 0
	for _, x := range nums {
		if idx < k || nums[idx-k] != x {
			nums[idx] = x
			idx += 1
		}
	}
	return idx
}
