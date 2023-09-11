class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '[':']', '{':'}'}
        stack = []
        for ch in s:
            if ch in dict:
                stack.append(ch)
            elif len(stack) == 0 or dict[stack.pop()] != ch:
                return False
        return len(stack) == 0

