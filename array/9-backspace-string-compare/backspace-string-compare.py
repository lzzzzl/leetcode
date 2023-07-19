class Solution1:
    """解法一: 堆栈
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        def process_string(str):
            stack = []
            for char in str:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)

        return process_string(s) == process_string(t)


class Solution2:
    """解法二: 快慢指针
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        s, t = list(s), list(t)
        s_slow = t_slow = 0
        
        for fast, x in enumerate(s):
            if x == '#':
                if s_slow != 0:
                    s_slow -= 1
                continue
            if s_slow != fast: s[s_slow] = s[fast]
            s_slow += 1
        
        for fast, x in enumerate(t):
            if x == '#':
                if t_slow != 0:
                    t_slow -= 1
                continue
            if t_slow != fast: t[t_slow] = t[fast]
            t_slow += 1

        return s[:s_slow] == t[:t_slow]
