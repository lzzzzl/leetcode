package main

type Solution1 struct{}

func (s Solution1) mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	left, right := 0, x
	for left <= right {
		middle := left + (right-left)/2
		if middle*middle <= x && x < (middle+1)*(middle+1) {
			return middle
		} else if x < middle*middle {
			right = middle - 1
		} else {
			left = middle + 1
		}
	}
	return -1
}

type Solution2 struct{}

func (s Solution2) mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	left, right := 0, x+1
	for left < right {
		middle := left + (right-left)/2
		if middle*middle <= x && x < (middle+1)*(middle+1) {
			return middle
		} else if x < middle*middle {
			right = middle
		} else {
			left = middle + 1
		}
	}
	return -1
}

type Solution3 struct{}

func (s Solution3) mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	y := x / 2
	for y*y > x {
		y = (y + x/y) / 2
	}
	return int(y)
}
