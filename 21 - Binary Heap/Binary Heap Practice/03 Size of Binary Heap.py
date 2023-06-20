class Binary_Heap:
    def __init__(self, size):
        self.binary_heap = (size + 1) * [None]
        self.heap_size = 0
        self.maximum_size = size + 1

    def __repr__(self):
        values = [value for value in self.binary_heap]
        return str(values)


def peek(root_node):
    if not root_node:
        return
    else:
        return root_node.binary_heap[1]


def size_of_heap(root_node):
    if not root_node:
        return
    else:
        return root_node.heap_size

new_bianry_heap = Binary_Heap(9)

if __name__ == "__main__":
    print(new_bianry_heap.heap_size)

