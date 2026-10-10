"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
sub-tasks:
1. recognise a conflict -> must be sorted by start times
2. count of how many meetings occurring at each time

[0, 5, 15]
[10, 20, 40]

(10,10) (10, 30) (20,20)
[10, 10, 20]
[10, 20, 30]

time: O(nlogn)
space: O(n)

min: 1 meeting room
max: n meeting rooms where n is len(intervals)
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meeting_rooms = 0
        max_rooms = 0
        start = sorted([x.start for x in intervals])
        end = sorted ([x.end for x in intervals])


        start_ptr = 0
        end_ptr = 0

        print(start, end)
        while start_ptr < len(start):
            if start[start_ptr] < end[end_ptr]:
                meeting_rooms += 1
                start_ptr += 1
            else:
                meeting_rooms -= 1
                end_ptr += 1

            max_rooms = max(meeting_rooms, max_rooms)

        return max_rooms



