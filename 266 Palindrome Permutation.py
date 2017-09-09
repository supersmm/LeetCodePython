'''
Given a string, determine if a permutation of the string could form a palindrome.
For example,
"code" -> False, "aab" -> True, "carerac" -> True.
'''
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        count = 0
        for char in s:
            d[char] = d.get(char, 0) + 1
        for j in d.values():
            count += j%2
        return True if count <= 1 else False

def canPermutePalindrome(self, s):
    return sum(v % 2 for v in collections.Counter(s).values()) < 2