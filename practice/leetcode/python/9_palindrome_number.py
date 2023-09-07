#https://leetcode.com/problems/palindrome-number/

#Given an integer x, return true if x is a palindrome, and false otherwise.
class Solution:
    def isNumberPalindrome(self, num: int) -> bool:
        if num < 0: return False
        div = 1
        while num > div * 10:
            div *= 10

        while num:
            right = num % 10
            left = num // div
            if left != right: return False
            num = (num % div) // 10
            div = div // 100

        return True
