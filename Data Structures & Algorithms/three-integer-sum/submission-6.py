class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums.sort()

        for i in range(len(nums)):
            item = nums[i]
            #can't find triplets larger than 0 that add to 0
            if item > 0:
                break
            
            if i > 0 and item == nums[i-1]:
                continue

            st, end = i+1, len(nums) -1

            while st < end:
                ThreeSum = nums[st] + nums[end] + item
                if ThreeSum > 0:
                    end -= 1
                elif ThreeSum < 0:
                    st += 1
                else:
                    result.append([nums[st], nums[end], item])
                    st+=1 
                    end-=1
                    while nums[st] == nums[st-1] and st < end:
                        st +=1
            
        return result
