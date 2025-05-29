from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, entry, sum):
            if sum == target:
                result.append(entry.copy())
                return
            if sum > target or i >= len(candidates):
                return

            entry.append(candidates[i])
            dfs(i, entry, sum + candidates[i])
            entry.pop()
            dfs(i+1, entry, sum)
        dfs(0, [], 0)
        return result


    def combinationSumIII(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, entry, sum):
            if sum == target:
                result.append(entry.copy())
                return
            if sum > target or i >= len(candidates):
                return

            entry.append(candidates[i])
            dfs(i, entry, sum+candidates[i])
            entry.pop()
            dfs(i+1, entry, sum)

        dfs(0, [], 0)
        return result

    def combinationSumIII(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, entry, sum):
            if sum == target:
                result.append(entry.copy())
                return

            if sum > target or i >= len(candidates):
                return

            entry.append(candidates[i])
            dfs(i, entry, sum+candidates[i])
            entry.pop()
            dfs(i+1, entry, sum)

        dfs(0, [], 0)
        return result

    def combinationSumII(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for candidate in candidates:
            for t in range(target+1):
                if candidate < t:
                    for res in dp[t - candidate]:
                        dp[t].append(res+[candidate])
                elif candidate == t:
                    dp[t].append([candidate])
        return dp[target]

    def combinationSumIV(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target+1)]
        for candidate in candidates:
            for t in range(target+1):
                if candidate < t:
                    for res in dp[t - candidate]:
                        dp[t].append(res + [candidate])
                elif candidate == t:
                    dp[t].append([candidate])
        return dp[target]
