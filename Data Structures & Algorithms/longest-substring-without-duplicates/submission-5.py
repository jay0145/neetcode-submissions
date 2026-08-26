class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashset = set()
        maxL = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] in hashset:
                while s[r] in hashset:
                    hashset.remove(s[l])
                    l +=1 
            hashset.add(s[r])
            r+=1
            
            maxL = max(maxL, r-l)
            

        return maxL