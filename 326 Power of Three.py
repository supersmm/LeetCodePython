'''
Given an integer, write a function to determine if it is a power of three.
'''
# 1 Loop Iteration: time complexity O(log3(n)), space complexity O(1)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n%3 == 0: # % Modulus, // Floor Division
            n /= 3
            return self.isPowerOfThree(n)
        return False
        
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n%3 == 0:
            n /= 3
        return n == 1
        
#  never use == when comparing doubles.