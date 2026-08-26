class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numdict = {}
        for i in nums: 
            if i in numdict.keys():
                return True
            else:
                numdict[i] = 1
        return False