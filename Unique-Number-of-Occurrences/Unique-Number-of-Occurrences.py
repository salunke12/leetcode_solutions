class Solution(object):
    def uniqueOccurrences(self, arr):
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] = hashmap[i] + 1
            else:
                hashmap[i] = 1
        set1 = set(hashmap.values())
        if len(set1) == len(hashmap.values()):
            return True 
        return False


        