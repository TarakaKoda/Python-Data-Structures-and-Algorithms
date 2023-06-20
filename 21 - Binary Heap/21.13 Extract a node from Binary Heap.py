class Binary_Heap:
    def __init__(self, size):
        self.binary_heap = (size + 1) * [None]
        self.heap_size = 0
        self.maximum_size = size+1

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
        inOrder_traversal(root_node, index*2 +1)

def postOrder_traversal(root_node, index):
    if not root_node.binary_heap:
        return print("Binary Heap does not exist")
    if index <= root_node.heap_size:
        postOrder_traversal(root_node, index*2)
        postOrder_traversal(root_node, index*2 +1)
        print(root_node.binary_heap[index])

def levelOrder_traversal(root_node):
    if not root_node.binary_heap:
        return print("Binary Heap does not exist")
    else:
        for i in  range(1, root_node.heap_size+1):
            print(root_node.binary_heap[i])

def heapify_tree_insert(root_node, index, heap_type):
    parent_node = int(index/2)
    if index <=1:
        return
    elif heap_type == "Min":
        if root_node.binary_heap[index] < root_node.binary_heap[parent_node]:
            root_node.binary_heap[index], root_node.binary_heap[parent_node] = root_node.binary_heap[parent_node], root_node.binary_heap[index]
        heapify_tree_insert(root_node, parent_node, heap_type)
    elif heap_type == "Max":
        if root_node.binary_heap[index] > root_node.binary_heap[parent_node]:
            root_node.binary_heap[index], root_node.bianry_heap[parent_node] = root_node.binary_heap[parent_node], root_node.bianry_heap[index]
        heapify_tree_insert(root_node, parent_node, heap_type)

def insert(root_node, value, heap_type):
    if root_node.heap_size + 1 == root_node.maximum_size:
        return "heap is full"
    root_node.binary_heap[root_node.heap_size+1] = value
    root_node.heap_size += 1
    heapify_tree_insert(root_node, root_node.heap_size, heap_type)
    return "insertion is successful"


def heapify_tree_extract(root_node, index, heap_type):
    left_child = index * 2
    right_child = index * 2 + 1
    swap_child = 0

    if root_node.heap_size < left_child:
        return
    elif root_node.heap_size == left_child:
        if heap_type == "Min":
            if root_node.binary_heap[index] > root_node.binary_heap[left_child]:
                root_node.binary_heap[index], root_node.binary_heap[left_child] = root_node.binary_heap[left_child], root_node.binary_heap[index]
            return
        else:
            if root_node.binary_heap[index] < root_node.binary_heap[left_child]:
                root_node.binary_heap[index], root_node.binary_heap[left_child] = root_node.binary_heap[left_child], root_node.binary_heap[index]
            return

    else:
        if heap_type == "Min":
            if root_node.binary_heap[left_child] > root_node.binary_heap[right_child]:
                swap_child = right_child
            else:
                swap_child = left_child
            if root_node.binary_heap[index] > root_node.binary_heap[swap_child]:
                root_node.binary_heap[index], root_node.binary_heap[swap_child] = root_node.binary_heap[swap_child], root_node.binary_heap[index]
        else:
            if root_node.binary_heap[left_child] < root_node.binary_heap[right_child]:
                swap_child = right_child
            else:
                swap_child = left_child
            if root_node.binary_heap[index] < root_node.binary_heap[swap_child]:
                root_node.binary_heap[index], root_node.binary_heap[swap_child] = root_node.binary_heap[swap_child], root_node.binary_heap[index]
    heapify_tree_extract(root_node, swap_child, heap_type)


def extract(root_node, heap_type):
    if root_node.heap_size == 0:
        return
    else:
        extract_node = root_node.binary_heap[1]
        root_node.binary_heap[1] = root_node.binary_heap[root_node.heap_size]
        root_node.binary_heap[root_node.heap_size] = None
        root_node.heap_size -= 1
        heapify_tree_extract(root_node, 1, heap_type)
        return extract_node


new_binary_heap = Binary_Heap(6)

if __name__ == "__main__":
    insert(new_binary_heap, 2, "Min")
    insert(new_binary_heap, 5, "Min")
    insert(new_binary_heap, 7, "Min")
    insert(new_binary_heap, 1, "Min")
    extract(new_binary_heap, "Min")
    preOrder_traversal(new_binary_heap, 1)
