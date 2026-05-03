class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr = []
        for i in range(0,len(candies)):
            temp = extraCandies + candies[i]
            count = 0
            for j in range(0,len(candies)):
                if temp >= candies[j]:
                    count += 1
                    if count == len(candies):
                        arr.append(True) 
            if count != len(candies):
                arr.append(False)
        return arr