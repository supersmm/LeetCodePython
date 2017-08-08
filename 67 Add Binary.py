class Solution(object):
# int function with base=2, or eval function with '0b'
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a,2) + int(b,2))[2:]

# Mathematical calculation with recursion
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if not b: return a
        if not a: return b
        if a[-1] == b[-1] == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]),'1') + '0'
        if a[-1] == b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'