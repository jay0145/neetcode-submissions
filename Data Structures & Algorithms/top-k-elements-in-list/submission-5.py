class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### SAMPLE ANSWER TEST
        count = defaultdict(int)
        freqList = [[] for i in range(len(nums)+ 1)]
        result = []

        for num in nums:
            count[num]+= 1
        
        for num, freq in count.items():
            freqList[freq].append(num)

        for index in range(len(freqList) -1, 0, -1):
            for item in freqList[index]:
                result.append(item)
                if len(result) == k:
                    return result