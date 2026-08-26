class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        hashset = set()
        maxL = 0

        l = 0
        r = 0

        while r < len(s): 
            while s[r] in hashset:
                hashset.remove(s[l])
                l +=1 
            hashset.add(s[r])
            r+=1
            
            maxL = max(maxL, r-l)
            

        return maxL