class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

#bin(): Convert an integer number to a binary string.
return bin(x^y).count('1')