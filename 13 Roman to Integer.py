class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conv_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        if n < 2:
            return conv_dict[s]
        res = conv_dict[s[0]]
        for i in range(1, n):
            last = conv_dict[s[i-1]]
            curr = conv_dict[s[i]]
            if last < curr:
                res = res - 2*last + curr
            else:
                res += curr
        return res