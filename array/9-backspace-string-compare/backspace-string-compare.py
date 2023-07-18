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
