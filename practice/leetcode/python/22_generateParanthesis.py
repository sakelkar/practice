from typing import List
class Solution:
    def generateParanthesis(self, n: int) -> List[str]:
        result = []
        def dfs(left, right, s):
            if len(s) == 2*n:
                result.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right+1, s + ')')
        dfs(0, 0, '')
        return result

