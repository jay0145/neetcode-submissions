class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        res = ""

        tDict = {}
        for i in t:
            if i in tDict:
                tDict[i] += 1
                continue
            tDict[i] = 1
        #print(tDict)

        tempDict = {}

        l = 0
        matches = 0
        t_chars = len(tDict)
        for r in range(len(s)):
            char = s[r]
            if char in tDict:
                tempDict[char] = tempDict.get(char, 0) + 1
                if tempDict[char] == tDict[char]:
                    matches += 1
            
            #print(f"l, r: {l}, {r} = {s[l]} {s[r]} - m={matches} - {tempDict}")
            while matches == t_chars:
                #print("entered while")
                if (len(res)== 0 or len(res) > r - l + 1):
                    res = s[l: r+1]
                    #print(f"res {res}")
                char_l = s[l]
                if char_l in tDict:
                    if tempDict[char_l] == tDict[char_l]:
                        matches -= 1
                    tempDict[char_l] -= 1
                        #print("match deducted")
                l +=1


        return res