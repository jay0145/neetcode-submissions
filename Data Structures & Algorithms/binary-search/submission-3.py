class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        l = 0
        r = len(nums)-1

        while l <= r :
            index = (r + l) // 2
            #print(index)
            if nums[index] == target:
                return index
            elif nums[index] > target: 
                r = index - 1
            else:
                l = index + 1


        return -1