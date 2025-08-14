# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        my_dict = {}
        for letter in s:
            my_dict[letter] = my_dict.get(letter,0) + 1
        length = 0
        flag = False

        for count in my_dict.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                flag = True
        return length + 1 if flag else length
            