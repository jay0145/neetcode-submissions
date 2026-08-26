class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        hmap = {
            "{": "}",
            "[": "]",
            "(":  ")"
        }

        stack = []

        for i in range(0, len(s)):
            if s[i] in hmap:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                print(f"{hmap[temp]} and {s[i]}")
                if hmap[temp] != s[i]:
                    return False            
        return not stack