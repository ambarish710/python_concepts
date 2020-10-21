# 253. Meeting Rooms II
#
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
#
# Example 1:
#
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
#
# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


# Logic -- Priority Queues


from collections import deque


class Solution:
    def minMeetingRooms(self, intervals):
        queue_list = []
        rooms = 0

        def my_sort_func(x):
            return x[0], x[1]

        intervals.sort(key=my_sort_func)

        for interval in intervals:
            if queue_list == []:
                queue = deque()
                queue.append(interval)
                queue_list.append(queue)
                rooms += 1
            else:
                flag = 1
                for q in queue_list:
                    if q[-1][1] <= interval[0]:
                        q.append(interval)
                        flag -= 1
                        break
                if flag == 1:
                    queue = deque()
                    queue.append(interval)
                    queue_list.append(queue)
                    rooms += 1
        return rooms