'''
In a binary search tree (BST), the time complexity for inserting a value is indeed O(log n) on average. This is because
the BST is a binary tree structure that maintains a specific ordering property: for every node, all values in its left
subtree are smaller, and all values in its right subtree are larger.

When inserting a new value into the BST, the algorithm traverses the tree from the root downward, comparing the new
value with the values at each node. Based on the comparison, it decides whether to go left or right to continue the search.
By following this process, the algorithm can find the appropriate position to insert the new value in the tree.

The reason why the time complexity is O(log n) is that, on average, each comparison reduces the search space by half.
In a balanced BST, where the tree is evenly distributed and has a height of log n (where n is the number of nodes), the
algorithm needs to make approximately log n comparisons to find the correct position. Since the height of a balanced BST
is logarithmic in the number of nodes, the time complexity for insertion is O(log n).

However, it's important to note that the time complexity of BST operations, including insertion, heavily relies on the
tree's balance. In the worst case scenario, where the tree is highly unbalanced (resembling a linked list), the time
complexity for insertion can degrade to O(n), as the tree's height becomes equal to the number of nodes. To mitigate
this issue, various self-balancing BST implementations, such as AVL trees or Red-Black trees, are used to maintain
balance and ensure efficient operations.

In a binary search tree (BST), the worst-case time complexity for insertion is indeed O(n) if the tree becomes highly
unbalanced. To understand why, consider a scenario where you insert values in strictly ascending or descending order
into the BST. In this case, the tree will resemble a linked list, with each new node being appended to the right or left
side of the existing nodes.

When the BST is highly unbalanced, its height becomes equal to the number of nodes, which is n. In such a situation, the
time complexity for insertion becomes O(n) because you may need to traverse the entire height of the tree to find the
appropriate position for insertion.

To address this issue and ensure efficient operations, self-balancing BST implementations such as AVL trees or Red-Black
trees are used. These data structures maintain balance by dynamically adjusting the tree's structure during insertion and
deletion operations. By keeping the tree balanced, they limit the height of the tree to a logarithmic value, allowing
for efficient searching, insertion, and deletion with a time complexity of O(log n).

In summary, the time complexity of O(log n) for insertion in a binary search tree assumes the tree is balanced. In the
worst case scenario of an unbalanced tree, the time complexity can degrade to O(n). Self-balancing BST implementations
mitigate this issue and guarantee efficient operations regardless of the input order of values.
'''

class Binary_Search_Tree:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def insert(root_node, value):
    if root_node.data is None:
        root_node.data = None
    elif value <= root_node.data:
        if root_node.left_child is None:
            root_node.left_child = Binary_Search_Tree(value)
        else:
            insert(root_node.left_child, value)
    else:
        if root_node.right_child is None:
            root_node.right_child = Binary_Search_Tree(value)
        else:
            insert(root_node.right_child, value)
    return "New value is successfully inserted"

binary_search_tree = Binary_Search_Tree(80)

if __name__ == "__main__":
    print(insert(binary_search_tree,50))
    print(insert(binary_search_tree,60))
    print(binary_search_tree.data)
    print(binary_search_tree.left_child.data)


