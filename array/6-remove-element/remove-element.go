package main

type Solution1 struct{}

func (s Solution1) removeElement(nums []int, val int) int {
	i := 0
	n := len(nums)
	for i < n {
		if nums[i] == val {
			nums[i] = nums[n-1]
			n -= 1
		} else {
			i += 1
		}
	}
	return n
}

type Solution2 struct{}

func (s Solution2) removeElement(nums []int, val int) int {
	fast := 0
	slow := 0
	for fast < len(nums) {
		if nums[fast] != val {
			nums[slow] = nums[fast]
			slow += 1
		}
		fast += 1
	}
	return slow
}

type Solution3 struct{}

func (s Solution3) removeElement(nums []int, val int) int {
	i := 0
	for j := 0; j < len(nums); j++ {
		if nums[j] != val {
			nums[i] = nums[j]
			i += 1
		}
	}
	return i
}
