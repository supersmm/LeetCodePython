class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        n = len(s)
        if n < 2:
            return []
        for i in range(1, n):
            if s[i-1] == s[i] == '+':
                res.append(s[:i-1] + '--' + s[i+1:])
        return res