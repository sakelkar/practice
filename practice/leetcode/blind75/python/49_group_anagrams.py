#Given an array of strings strs, group the together. You can return the answer in any order.
#
#Example 1:
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Explanation:
#    There is no string in strs that can be rearranged to form "bat".
#    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#
#Example 2:
#Input: strs = [""]
#Output: [[""]]
#
#Example 3:
#Input: strs = ["a"]
#Output: [["a"]]
#
#Constraints:
#    1 <= strs.length <= 104
#    0 <= strs[i].length <= 100
#    strs[i] consists of lowercase English letters.

from collections import defaultdict
from typing import List


class Solutions:
    def groupAnagrams(self, strs: List[str]) -> List[List[int]]:
        #define the dictionary such that for key string type value is list of strs
        #define the default value of type list and it will be empty()
        maps = defaultdict(list)
        for s in strs:
            hash = sorted(s)
            maps[hash].append(s)
        return list(maps.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[int]]:
        used = [False] * len(strs)
        answer = []

        for i, s in enumerate(strs):
            if not used[i]:
                entry = [s]
                used[i] = True
                for j in range(i+1, len(strs)):
                    if not used[j] and sorted(s) == sorted(strs[j]):
                        used[j] = True
                        entry.append(strs[j])
                answer.append(entry)
        return answer

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        used = [False] * len(strs)
        answer = []
        for i, s in enumerate(strs):
            if not used[i]:
                used[i] = True
                entry = [s]
                for j in range(i+1, len(strs)):
                    if not used[j] and sorted(s) == sorted(strs[j]):
                        used[i] = True
                        entry.append(strs[j])
                answer.append(entry)
        return answer
