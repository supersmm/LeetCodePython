#brute force
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_haystack = len(haystack)
        n_needle = len(needle)
        if n_needle == 0:
            return 0
        if n_haystack < n_needle:
            return -1
        for i in range(n_needle, n_haystack+1):
            if haystack[i-n_needle: i] == needle:
                return i-n_needle
        return -1

#two pointers
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n_haystack = len(haystack)
        n_needle = len(needle)
        if n_haystack < n_needle:
            return -1
        slow = 0
        for fast in range(n_needle, n_haystack+1):
            if haystack[slow: fast] == needle:
                return slow
            slow += 1
        return -1