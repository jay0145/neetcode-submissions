class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        pref = [0] * n
        suff = [0] * n
        res = [0] * n


        for i in range(n):
            if i == 0:
                pref[i] = 1
            else:
                pref[i] = nums[i-1] * pref[i-1]

        for i in range(n-1, -1, -1):
            if i == n-1:
                suff[i] = 1
            else:
                suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]

        return res