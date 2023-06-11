'''
How to use collections.deque as a FIFO queue:
- one this in deque if we want to add elements exceeding the size of the queue then it will automatically delete the first
  element and adds the new value at the end the list
'''
from collections import deque

queue = deque(maxlen=3)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
print(queue.popleft())
queue.clear()
print(queue)