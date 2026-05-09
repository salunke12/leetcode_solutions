class Solution(object):
    def isSubsequence(self, s, t):
        if not s:
            return True

        index = 0
        for j in t:
            if index < len(s) and s[index] == j:
                index +=1
            if index == len(s):
                return True
        return False