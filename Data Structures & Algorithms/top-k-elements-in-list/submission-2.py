class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        count = []
        for i in range(len(nums)+1):
            count.append([])

        for i, j in freq.items():
            count[j].append(i)
        
        l = []
        for i in range(len(count)-1, 0, -1):
            for num in count[i]:
                l.append(num)
                if len(l) == k:
                    return l