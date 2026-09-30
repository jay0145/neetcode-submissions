class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramDict = defaultdict(list)

        for string in strs:
            count = [0]*26

            for char in string:
                index = ord(char) - ord('a')
                count[index] += 1

            charFreq = tuple(count)
            anagramDict[charFreq].append(string)
        
        return list(anagramDict.values())