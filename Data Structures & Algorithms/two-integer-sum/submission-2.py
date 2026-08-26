class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        st = 0
        en = 1
        while st != len(nums)-1:
            if nums[st] + nums[en] == target:
                return [st, en]
            if en != len(nums)-1:
                en+=1
            else:
                st +=1 
                en = st + 1