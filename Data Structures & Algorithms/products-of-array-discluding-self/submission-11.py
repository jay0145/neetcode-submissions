class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Solution with O(1) space complexity
        #And O(n) time complexity

        n = len(nums)

        res = [0] * n

        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]

        post = nums[n-1]
        for i in range(n-2, -1, -1):
            res[i] = res[i] * post
            post = post * nums[i]

        return res