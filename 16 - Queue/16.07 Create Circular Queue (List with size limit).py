class Queue:
    def __init__(self, max_value):
        self.items = max_value * [None]
        self.max_value = max_value
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)


queue = Queue(6)

if __name__ == "__main__":
    print(queue)