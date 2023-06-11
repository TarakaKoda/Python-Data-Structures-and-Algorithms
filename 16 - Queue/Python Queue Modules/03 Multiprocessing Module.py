'''
The Queue class from the multiprocessing module is designed to be process-safe, meaning it can be safely used across
multiple processes without causing race conditions or data corruption.
'''

import multiprocessing as mp

queue = mp.Queue(maxsize=3)

if __name__ == "__main__":
    print(queue.empty())
    queue.put(1)
    queue.qsize()
    queue.put(2)
    queue.put(3)
    print(queue.get())
    print(queue.get())
    print(queue.qsize())