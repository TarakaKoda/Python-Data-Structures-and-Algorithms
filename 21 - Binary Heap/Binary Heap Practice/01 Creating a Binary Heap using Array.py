class Binary_Heap:
    def __init__(self, size):
        self.binary_heap = (size+1) * [None]
        self.heap_size = 0
        self.maximum_size = size + 1

    def __repr__(self):
        values = [value for value in self.binary_heap]
        return str(values)


new_binary_heap = Binary_Heap(3)

if __name__ == "__main__":
    print(new_binary_heap)

