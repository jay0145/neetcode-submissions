class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            dic[s[r]] += 1
            mostfreq = max(dic.values())
            while (r-l+1) - mostfreq > k and l <= r:
                dic[s[l]] -= 1
                l += 1
            res = max(res, r - l+1)

        return res