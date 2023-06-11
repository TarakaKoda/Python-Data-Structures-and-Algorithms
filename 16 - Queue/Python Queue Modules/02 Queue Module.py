'''
    In Python, you can use the built-in queue module from the standard library to create different types of queues, such as
    FIFO queues, LIFO queues (stacks), and priority queues. Here's a brief overview of how you can use the queue module for
    each type:

    FIFO Queue:
    - Import the queue module: import queue
    - Create a FIFO queue object: my_queue = queue.Queue()
    - Add elements to the queue: my_queue.put(item)
    - Remove elements from the queue (in FIFO order): item = my_queue.get()

    LIFO Queue (Stack):
    - Import the queue module: import queue
    - Create a LIFO queue object: my_stack = queue.LifoQueue()
    - Add elements to the stack: my_stack.put(item)
    - Remove elements from the stack (in LIFO order): item = my_stack.get()

    Priority Queue:
    - Import the queue module: import queue
    - Create a priority queue object: my_priority_queue = queue.PriorityQueue()
    - Add elements to the priority queue, specifying their priority: my_priority_queue.put((priority, item))
      (The priority can be any number or a comparable object, where lower values indicate higher priority.)
    - Remove elements from the priority queue (in order of priority): item = my_priority_queue.get()

    Note that the queue module provides thread-safe implementations of these queues, making them suitable for concurrent
    programming scenarios. If you don't require thread safety, you can also use the collections.deque class from the
    standard library, which provides a non-thread-safe double-ended queue implementation that can be used as a FIFO queue or
    a LIFO stack.
'''

import queue as q

queue = q.Queue(maxsize=3)

if __name__ == "__main__":
    print(__doc__)
    print(queue.empty())
    queue.put(1)
    queue.put(3)
    queue.put(2)
    print(queue.get())
    print(queue.full())
    print(queue.qsize())



