class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        # Quick exit if no flowers need to be planted
        if n == 0:
            return True
            
        for i in range(len(flowerbed)):
            # Check if current spot is empty
            if flowerbed[i] == 0:
                # Check left: True if we're at index 0 OR the left neighbor is 0
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Check right: True if we're at the last index OR the right neighbor is 0
                next_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    n -= 1
                    
                    # If we've placed all needed flowers, we can stop early
                    if n <= 0:
                        return True
                        
        return n <= 0