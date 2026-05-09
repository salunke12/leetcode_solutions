class Solution(object):
    def reverseVowels(self, s):
        char = list(s)
        vowels = set('aeiouAEIOU')
        index = [] 
        for i in range(0,len(s)):
            if char[i] in vowels:
                index.append(i)
        l = 0
        r = len(index)-1
        while l<r:
            a = index[l]
            b = index[r]
            char[a],char[b]= char[b],char[a]
            l +=1
            r -=1
        s= "".join(char)
        return s