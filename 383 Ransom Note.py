class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        def constructDict(s):
            sDict = {}
            for i in s:
                if sDict.get(i): 
                    sDict[i] += 1
                else: 
                    sDict[i] = 1
            return sDict
        ransomDict = constructDict(ransomNote)
        magazineDict = constructDict(magazine)
        for k, v in ransomDict.items():
            if not magazineDict.get(k):
                return False
            if magazineDict[k] < v:
                return False
        return True
        
def canConstruct(self, ransomNote, magazine):
    return not collections.Counter(ransomNote) - collections.Counter(magazine)
    
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))	# or c in string.ascii_lowercase