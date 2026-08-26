class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = defaultdict(int)

        for i in nums:
            mapping[i] += 1
        
        out = sorted(list(mapping.items()), key=lambda item: item[1], reverse=True)[:k]

        print(out)
        l = []
        for i in out:
            l.append(i[0])
        return l
