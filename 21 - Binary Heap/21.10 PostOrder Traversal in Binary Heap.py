class Binary_Heap:
    def __init__(self, size):
        self.binary_heap = (size+1) * [None]
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

def preOrder_traversal(root_node, index):
    if not root_node.binary_heap:
        return print("Binary Heap does not exist")
    if index <= root_node.heap_size:
        print(root_node.binary_heap[index])
        preOrder_traversal(root_node, index*2)
        preOrder_traversal(root_node, index*2 + 1)

def inOrder_traversal(root_node, index):
    if not root_node.binary_heap:
        return print("Binary Heap does not exist")
    if index <= root_node.heap_size:
        inOrder_traversal(root_node, index*2)
        print(root_node.binary_heap[index])
        inOrder_traversal(root_node, index*2 + 1)

def postOrder_traversal(root_node, index):
    if not root_node.binary_heap:
        return print("Binary Heap does not exist")
    if index <= root_node.heap_size:
        postOrder_traversal(root_node, index*2)
        postOrder_traversal(root_node, index*2 +1)
        print(root_node.binary_heap[index])

new_binary_heap = Binary_Heap(6)

if __name__ == "__main__":
    new_binary_heap.binary_heap[1] = 2
    new_binary_heap.binary_heap[2] = 5
    new_binary_heap.binary_heap[3] = 10
    new_binary_heap.binary_heap[4] = 4
    new_binary_heap.binary_heap[5] = 3
    new_binary_heap.binary_heap[6] = 9
    new_binary_heap.heap_size = 6
    postOrder_traversal(new_binary_heap, 1)