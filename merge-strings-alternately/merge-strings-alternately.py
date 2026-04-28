class Solution(object):
    def mergeAlternately(self, word1, word2):
        str1=""
        for i in range(0,max(len(word1),len(word2))):
            if i< len(word1):
                str1 = str1 + word1[i]
            if i< len(word2):
                str1 = str1 + word2[i]
            
        return str1