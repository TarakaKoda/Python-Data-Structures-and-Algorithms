class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)


queue = Queue()
queue.items = [1,2,3,4,5]

if __name__ == "__main__":
    print(queue)