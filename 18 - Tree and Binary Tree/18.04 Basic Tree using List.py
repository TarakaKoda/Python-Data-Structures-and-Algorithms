'''
How to create a basic tree structure in python using list
Note: Alcohol is bad for health please try to avoid them :)
'''

class Tree_Node:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        result = " " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def add_child(self, tree_node):
        self.children.append(tree_node)


tree = Tree_Node("Drinks", [])
cold = Tree_Node("cold", [])
hot = Tree_Node("hot", [])
tree.add_child(cold)
tree.add_child(hot)
alcoholic = Tree_Node("Alcoholic", [])
non_alcoholic = Tree_Node("Non-Alcoholic", [])
cold.add_child(alcoholic)
cold.add_child(non_alcoholic)
tea = Tree_Node("Tea", [])
coffee = Tree_Node("Coffee", [])
hot.add_child(tea)
hot.add_child(coffee)
beer = Tree_Node("Beer", [])
wine = Tree_Node("Wine", [])
whiskey = Tree_Node("Whiskey", [])
vodka = Tree_Node("Vodka", [])
alcoholic.add_child(beer)
alcoholic.add_child(wine)
alcoholic.add_child(whiskey)
alcoholic.add_child(vodka)
soda = Tree_Node("Soda", [])
cola = Tree_Node("Cola", [])
fanta = Tree_Node("Fanta", [])
non_alcoholic.add_child(soda)
non_alcoholic.add_child(cola)
non_alcoholic.add_child(fanta)
print(tree)
