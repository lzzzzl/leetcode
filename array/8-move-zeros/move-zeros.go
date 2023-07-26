package main

type Solution1 struct{}

func (s Solution1) moveZeroes(nums []int) {
	slow := 0
	for fast := 0; fast < len(nums); fast++ {
		if nums[fast] != 0 {
			nums[slow], nums[fast] = nums[fast], nums[slow]
			slow += 1
		}
	}
}

type Solution2 struct{}

func (s Solution2) moveZeroes(nums []int) {
	i := 0
	j := 0
	for i < len(nums) {
		if nums[i] == 0 {
			nums = append(nums[:i], nums[i+1:]...)
			j++
			continue
		}
		i++
	}
	for k := 0; k < j; k++ {
		nums = append(nums, 0)
	}
}
