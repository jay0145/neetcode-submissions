"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
E.g.(1)

[(0,30), (5,10), (15,20)]

assumptions:
- start times in chronological order??
- minutes > 60? no up to 1,000,000 so units of time
- two items in tuple and no negative time

edge cases:
- [(5,10), (0,30)] - unsorted/encapsulated: important to be sorted
- [(0,10), (10,20)] - works!
- [(0,10), (15,30)] - spare time
- [(0,10), (7, 15)] - right merge
- [(10,20), (5,15)] - left merge

brute force:
- sort them by start time - if done don't do 
- time: O(n)
- space: O(1)

curr_start = 0
curr_end = 30

for st, en in intervals: 
    ## index=1 so st = 5, en = 10
    if st > curr_st or en < curr_end:
        return False
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        curr_start, curr_end = 0,0

        for item in sorted_intervals:
            print(curr_start, curr_end)

            st = item.start
            en = item.end

            if st < curr_end:
                return False

            curr_start = st
            curr_end = en


        return True
