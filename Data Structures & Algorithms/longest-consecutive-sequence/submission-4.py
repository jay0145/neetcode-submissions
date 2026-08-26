class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        snums = sorted(nums)
        result = 0
        a = set()

        #print(snums)
        for i in range(0, len(snums)-1):
            if snums[i] == (snums[i+1]-1):
                a.add(snums[i])
                a.add(snums[i+1])
                #print(f"a: {a}")
            elif snums[i] == snums[i+1]:
                continue
                #print('cont')
            else:
                #print('reset')
                if len(a) > result:
                    result = len(a)
                a.clear()

        if len(a) > result:
            result = len(a)
        
        if result==0 and len(snums)>0:
            return 1

        return result