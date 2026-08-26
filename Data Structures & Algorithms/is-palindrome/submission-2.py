class Solution:
    def isPalindrome(self, s: str) -> bool:
        validchars = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',   'q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','0','1','2','3','4','5','6','7','8','9'}

        strs = ""
        for i in range(len(s)):
            if s[i] in validchars:
                strs = f"{strs}{s[i]}"

        strs = strs.lower()

        st = 0
        end = len(strs)-1
        while st < end:
            if strs[st] != strs[end]:
                return False
            st += 1
            end -=1 
        
        return True
            