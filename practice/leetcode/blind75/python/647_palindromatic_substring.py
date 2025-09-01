#https://leetcode.com/problems/palindromic-substrings/description/
#
#Given a string s, return the number of palindromic substrings in it.
#A string is a palindrome when it reads the same backward as forward.
#A substring is a contiguous sequence of characters within the string.
#
#Example 1:
#
#Input: s = "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#
#Example 2:
#
#Input: s = "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

from re import X


class Solution:
    def countSubstring(self, s: str) -> int:
        def palindromeAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return(count)

        result = 0
        for center in range(len(s)):
            result += palindromeAroundCenter(center, center) #odd length palindrome string
            result += palindromeAroundCenter(center, center+1) #even length palindrome substring
        return(result)

    def countSubstring2(self, s: str) -> int:
        def palindromeAroundCenter(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        result = 0
        for center in range(len(s)):
            result += palindromeAroundCenter(center, center)
            result += palindromeAroundCenter(center, center+1)

    def countSubstringDP(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        count = 0

        table = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][i] = True
            count += 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        for k in range(3, n+1):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] == True and s[i] == s[j]:
                    table[i][j] = True
                    count += 1
        return count

    #countSubstringDP2
    def countSubstringDP2(self, s: str) -> int:
        if not s:
            return 0

        n = len(s)
        count = 0
        table = [[False] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            table[i][i] = True
            count += 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1

        for k in range(3, n+2):
            for i in range(n-k+1):
                j = i+k-1
                if table[i+1][j-1] == True and s[i] == s[j]:
                    table[i][j] = True
                    count += 1
        return count

