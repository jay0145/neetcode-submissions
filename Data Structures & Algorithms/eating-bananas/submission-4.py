'''
[2,4,3,2] h = 11 then k = 1 even if one of nums in piles

10/9 = 1.1 -> 2

62 / 4 = 15.5 -> 16
'''
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        minRate = piles[len(piles)-1]

        print(piles)

        l = 1
        r = piles[len(piles) - 1]

        while l <= r:
            
            rate = (l + r) // 2
            hours = 0

            print(rate)
            for bananas in piles:
                hours += math.ceil(bananas / rate)
            
            
            if h < hours:
                l = rate + 1
            
            if h >= hours:
                r = rate - 1
                minRate = min(rate, minRate)

        
        return minRate
                
                