# Task Scheduler
# Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.
#
# Example 1:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation:
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.
# Example 2:
#
# Input: tasks = ["A","A","A","B","B","B"], n = 0
# Output: 6
# Explanation: On this case any permutation of size 6 would work since n = 0.
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# And so on.
# Example 3:
#
# Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# Output: 16
# Explanation:
# One possible solution is
# A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
#
# Constraints:
#
# 1 <= task.length <= 104
# tasks[i] is upper-case English letter.
# The integer n is in the range [0, 100].

# ANSWER
# Algorithm
#
# The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
#
# Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
#
# Sort the array and retrieve the maximum frequency f_max. This frequency defines the max possible idle time: idle_time = (f_max - 1) * n.
#
# Pick the elements in the descending order one by one. At each step, decrease the idle time by min(f_max - 1, f) where f is a current frequency. Remember, that idle_time is greater or equal to 0.
#
# Return busy slots + idle slots: len(tasks) + idle_time.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurence = [0] * 26

        for character in tasks:
            occurence[ord(character) - ord("A")] += 1

        occurence.sort()

        frequency_max = occurence.pop()

        idle_time = (frequency_max - 1) * n

        while occurence and idle_time > 0:
            idle_time -= min(frequency_max - 1, occurence.pop())

        idle_time = max(0, idle_time)

        return len(tasks) + idle_time