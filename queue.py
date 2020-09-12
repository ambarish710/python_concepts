# Approach 1
# Creating queue data structures with list in python
queue = []
queue.insert(0, 5)
queue.insert(0, 10)
queue.insert(0, 15)
print(queue)
print(len(queue))
queue.pop()
print(queue)
print(len(queue))


# Approach 2
# Correct approach is by using deque -- deque can be used as stack as well as queue
# The reason being dynamic array limit reach issue
from collections import deque

class QueueClass:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        self.queue.pop()

    def queue_length(self):
        return len(self.queue)

if __name__ == "__main__":
    qc_obj =  QueueClass()
    qc_obj.enqueue(5)
    qc_obj.enqueue(10)
    qc_obj.enqueue(15)
    qc_obj.queue_length()
    print(qc_obj.queue)
    qc_obj.dequeue()
    qc_obj.queue_length()
    print(qc_obj.queue)
