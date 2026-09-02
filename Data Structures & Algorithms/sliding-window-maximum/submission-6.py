class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        dq = collections.deque()
        #print(dq)
        output = []
        
        for r in range(len(nums)):

            while dq and nums[r] > nums[dq[-1]]:
                dq.pop()
                #print(f"popped: {dq}")
            
            dq.append(r)
            
            if (r - k + 1) > dq[0]:
                dq.popleft()
            
            if (r+1) >= k:
                output.append(nums[dq[0]])
            #print(f"{r}: {dq}")
        
        return output
