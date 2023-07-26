package main

type Solution1 struct{}

func (s1 Solution1) processString(str string) string {
	stack := make([]rune, 0)
	for _, char := range str {
		if char != '#' {
			stack = append(stack, char)
		} else if len(stack) > 0 {
			stack = stack[:len(stack)-1]
		}
	}
	return string(stack)
}

func (s1 Solution1) backspaceCompare(s string, t string) bool {
	return s1.processString(s) == s1.processString(t)
}

type Solution2 struct{}

func (s2 Solution2) processString(str []rune) []rune {
	slow := 0
	for fast := range str {
		if str[fast] == '#' {
			if slow != 0 {
				slow--
			}
			continue
		}
		if slow != fast {
			str[slow] = str[fast]
		}
		slow++
	}
	return str[:slow]
}

func (s2 Solution2) backspaceCompare(s string, t string) bool {
	sRunes, tRunes := []rune(s), []rune(t)
	return string(s2.processString(sRunes)) == string(s2.processString(tRunes))
}
