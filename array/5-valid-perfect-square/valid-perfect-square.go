package main

type Solution1 struct{}

func (s Solution1) isPerfectSquare(num int) bool {
	if num == 1 {
		return true
	}
	left, right := 0, num-1
	for left <= right {
		middle := left + (right-left)/2
		if middle*middle > num {
			right = middle - 1
		} else if middle*middle < num {
			left = middle + 1
		} else {
			return true
		}
	}
	return false
}

type Solution2 struct{}

func (s Solution2) isPerfectSquare(num int) bool {
	if num == 1 {
		return true
	}
	x := num / 2
	for x*x > num {
		x = (x + num/2) / 2
	}
	return x*x == num
}
