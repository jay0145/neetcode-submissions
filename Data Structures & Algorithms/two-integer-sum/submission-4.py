class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for index, num in enumerate(nums):
            indices[num] = index

        for index, num in enumerate(nums):
            complement = target - num
            if complement in indices and indices[complement] != index:
                return [index, indices[complement]]