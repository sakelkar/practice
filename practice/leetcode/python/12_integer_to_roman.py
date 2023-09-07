#https://leetcode.com/problems/integer-to-roman/

#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

#For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#    I can be placed before V (5) and X (10) to make 4 and 9. 
#    X can be placed before L (50) and C (100) to make 40 and 90. 
#    C can be placed before D (500) and M (1000) to make 400 and 900.

#Given an integer, convert it to a roman numeral.

#Basic logic
#Craete a hash map of integer to roman
#Basically instead of division, roman numnerals progress based on subtraction. This is the key point
#So basically what you have to do is use lower_bound to find the cloest match in the hash-map
#if the lower_bound gives higher number then take one previous number in the has map than the current one
#if the lower bound is correct put in inside answer array
#new number = num - hash-map lookup result
#
#
class Solution:
    def intToRoman(self, num: int) -> str:
        convList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9],
                    ["X", 10], ["XL", 40], ["L", 50], ["XC", 90],
                    ["C", 100], ["CD", 400], ["D", 500], ["CM", 900],
                    ["M", 1000]]
        res = ""
        for sym, val in reversed(convList):
            if num // val:
                count = num // val
                res += (sym * count)
                num = num % val
        return(res)
