"""
count = 0

brute force:
for each element - is there overlapping, yes -> remove & +1 to count
time: O(nlogn)
space: O(n)

1. if there is an overlap
2. + 1 to count


[1,2] [1,4] [2,4] -> 
[1,2] [2,4] [1,4]

both lead to different answers if removing first overlap -> sort to normalise



"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        sorted_intervals = sorted(intervals, key= lambda x: x[0])

        prevEnd = sorted_intervals[0][1]

        for start, end in sorted_intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                count += 1
                prevEnd = min(prevEnd, end)

        return count