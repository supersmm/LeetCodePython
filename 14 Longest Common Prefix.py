# TypeError: object of type 'NoneType' has no len()
'''
>>> strs = ['Rocky','Robby','RoRo']
>>> zip(*strs)
<zip object at 0x03098E68>
>>> for i, j in enumerate(zip(*strs)):
...     print(i,j)
...
0 ('R', 'R', 'R')
1 ('o', 'o', 'o')
2 ('c', 'b', 'R')
3 ('k', 'b', 'o')
'''	
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
            
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
            
# Not accepted: ["",""] input returns null
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for i in range(1, len(strs)):
            ans = self.commonPrefix(ans, strs[i])
        return ans
    def commonPrefix(self, strA, strB):
        ans = ""
        try:
            for i in range(len(strA)):
                if strA[i] == strB[i]: ans += strA[i]
                else: return ans
        except (TypeError, IndexError):
            return ans