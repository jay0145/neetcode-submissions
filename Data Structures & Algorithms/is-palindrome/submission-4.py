class Solution:
    def isPalindrome(self, s: str) -> bool:

        st = 0
        end = len(s)-1

        while st < end:

            while not self.isAlphaNumeric(s[st]) and st < end:
                print(f'skipped{s[st]} at pos: {st}')
                st+=1
            while not self.isAlphaNumeric(s[end]) and st < end:
                print(f'skipped{s[end]} at pos:{end}')
                end-=1

            if s[st].lower() != s[end].lower():
                return False
            st += 1
            end -=1 
        
        return True

    def isAlphaNumeric(self, char: str) -> bool:
        if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9'):
            return True
        return False
            