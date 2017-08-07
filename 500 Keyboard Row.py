class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyboard = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,\
                    'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,\
                    'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3}
        
        def isOneRow(word):
            if len(word) <= 1:
                return True
            else:
                lower_word = word.lower()
                row = keyboard[lower_word[0]]
                for i in lower_word[1:]:
                    if keyboard[i] != row:
                        return False
                return True
            
        res = []
        for word in words:
            if isOneRow(word): 
                res.append(word)
        return res
        
def findWords(self, words):
    return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)
    
def findWords(self, words):
    line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
    ret = []
    for word in words:
      w = set(word.lower())
      if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
        ret.append(word)
    return ret