class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()

        for i in nums:
            numset.add(i)
        
        seq = 0
        for i in numset:
            if i-1 not in numset:
                streak = 0
                while i+streak in numset:
                    streak += 1
                if streak > seq:
                    seq = streak

        return seq