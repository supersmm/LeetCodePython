'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        d = {}
        for c in moves:
            d[c] = d.get(c, 0) + 1
        if d.get('U', 0) == d.get('D', 0) and d.get('L', 0) == d.get('R', 0):
            return True
        return False

def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')