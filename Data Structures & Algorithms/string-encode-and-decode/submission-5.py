class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            length = len(word)
            string += f"{length}*{word}"

        print(string)
        return string

    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0 
        while i < len(s):
            j = i
            while s[j] != "*":
                j += 1
            length = int(s[i:j]) #incase of double digit numbers
            i = j + 1
            j = i + length
            result.append(s[i:j])

            i=j

        return result