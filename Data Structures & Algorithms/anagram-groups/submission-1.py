class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        
        anaDict = {}

        for i in strs:
            item = ''.join(sorted(i))
            if item in anaDict:
                anaDict[item].append(i)
            else:
                anaDict[item] = [i]
        
        for i in anaDict.values():
            result.append(i)

        return result