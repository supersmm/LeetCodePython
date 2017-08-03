class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        res = 0
        while num > 0:
            res += num % 10
            num //= 10
        return self.addDigits(res)
 
'''
N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]. we set M = a[0] + a[1] + ..a[n]
and another truth is that: 1 % 9 = 1, 10 % 9 = 1, 100 % 9 = 1, so N % 9 = a[0] + a[1] + ..a[n]
means N % 9 = M, so N = M (% 9) also 9 % 9 = 0'''
class Solution(object):
	  def addDigits(self, num):
        return num % 9 or 9 if num else 0