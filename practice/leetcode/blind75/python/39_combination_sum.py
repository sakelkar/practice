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

    def combinationSumIV(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, entry, sum):
            if sum == target:
                answer.append(entry.copy())
                return
            if sum > sum or i >= len(candidates):
                return

            entry.append(candidates[i])
            dfs(i, entry, sum + candidates[i])
            entry.pop()
            dfs(i+1, entry, sum)

        dfs(0, [], 0)
        return answer

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

    def combinationSumVV(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, entry, sum):
            #edge cases for dfs are if the running sum for the dfs is = target
            if sum == target:
                result.append(entry.copy())
                return

            #or if the running sum > target or current running index beyond the length of the list
            if sum > target or i >= len(candidates):
                return

            #define dfs function in such a way that it will have two branches
            #first branch will take the current element and call dfs again
            #second branch will take the next element call dfs again
            entry.append(candidates[i])
            dfs(i, entry, sum + candidates[i])
            entry.pop()
            dfs(i+1, entry, sum)

        #start the dfs with first index and empry first entry and 0 as running sum
        dfs(0, [], 0)
        return result

    def combinationSumFinal(self, candidates: List[int], target: int) -> List[List[int]]:
        #define empry list as answer
        answer = []

        #dfs function
        def dfs(i, entry, sum):
            #boundry conditions
            #sum matches target
            if sum == target:
                answer.append(entry.copy())
                return

            #out of bounds or running sum is greater than target
            if i > len(candidates) or sum > target:
                return

            entry.append(candidates[i])
            #otherwise since repeatation is allowed take current and recurse
            dfs(i, entry, sum + candidates[i])

            #clear entry for without case
            entry.pop()
            #take next and recurse
            dfs(i + 1, entry, sum)

        #start recursion with index 0 and running sum as 0
        dfs(0, [], 0)
        return answer


