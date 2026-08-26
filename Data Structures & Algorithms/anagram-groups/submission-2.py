class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        anaDict = defaultdict(list)

        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c) - ord('a')] +=1 
            t = tuple(count)
            anaDict[t].append(i)

        return list(anaDict.values())