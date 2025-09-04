#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#    Open brackets must be closed by the same type of brackets.
#    Open brackets must be closed in the correct order.
#    Every close bracket has a corresponding open bracket of the same type.
#
#Example 1:
#Input: s = "()"
#Output: true

#Example 2:
#Input: s = "()[]{}"
#Output: true

#Example 3:
#Input: s = "(]"
#Output: false

#Example 4:
#Input: s = "([])"
#Output: true

#Example 5:
#Input: s = "([)]"
#Output: false
#
#Constraints:
#
#    1 <= s.length <= 104
#    s consists of parentheses only '()[]{}'.
class Solution:
    def isValid(self, s: str) -> bool:
        #define a dictionary or a map with start paranthesis as key and closing parenthesis as the value
        #since the opening and closing parenthesis sequence is expected to work like stack
        parenMap = {'{':'}', '[':']', '(':')'}
        stack = []
        for ch in s:
            #check if current character key exists in the parenMap
            if ch in parenMap:
                stack.append(ch)
            #else stack can never be empty or the current character by this time has to be equal to value in the map
            elif len(stack) == 0 or parenMap[stack.pop()] != ch:
                return False
        return(len(stack) == 0)


