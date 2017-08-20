class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        s = word[0].isupper()
        if s:
            return all(c.islower() for c in word[1:]) or all(c.isupper() for c in word[1:])
        return all(c.islower() for c in word[1:])    
        	
def detectCapitalUse(self, word):
    return word.isupper() or word.islower() or word.istitle()