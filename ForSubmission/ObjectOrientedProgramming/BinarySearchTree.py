class Node:
    def __init__(self, key, data):
        self.left_child = None
        self.right_child = None
        self.key = key
        self.data = data

    def insert_node(self, node):
        if node.key < self.key: # if the value of the new key is lower than the node key (first time - the root)
            if self.left_child is None: # the node doesnt have a left child 
                self.left_child = node #  insert the node as a left child
            else:
                self.left_child.insert_node(node) # that node has left_child, enter recursion, go a level down
        elif node.key > self.key: # we should not allow equality as Binary Search Tree cannot have identical keys
            if self.right_child is None:
                self.right_child = node
            else:
                self.right_child.insert_node(node)

    def get_node(self, key):
        if key < self.key:
            if self.left_child is None:
                return str(key) + " Not Found"
            return self.left_child.get_node(key)
        elif key > self.key:
            if self.right_child is None:
                return str(key) + " Not Found"
            return self.right_child.get_node(key)
        else:
            return self

    def __str__(self):
        return f"Key: {self.key}, Data: {self.data}"


tree = Node("Vahe", 40)
tree.insert_node(Node("Thomas", 45))
tree.insert_node(Node("Zeke", 123))
tree.insert_node(Node("Alex", 23))
tree.insert_node(Node("Ian", 66))

print(tree.get_node("Thomas"))
print(tree.get_node("Vahe"))
print(tree.get_node("Zeke"))
print(tree.get_node("Alex"))
print(tree.get_node("Al"))  # should return "Alex is not found"

    # Computational Complexity: 
    # The complexity would depend on the existing tree, if it is not balanced, in an extreme case where all nodes are on the same side (left or right) the complexity would be linear O(n). This would be the worst case.
    # For a perfectly balanced tree where all parent nodes have exactly two children and all leaves are on the same level, then the computational complexity would be O(log(n)) due to division in half (or the height of the tree).
    # The best case would have a constant complexity.
    # The same applies both for insertion and for retrieval

    # The order of insertion definely matters in terms of the layout of the tree itelf. the first item serves as the root, and the rest of the items are added to the respective free leaves (based on the check of the value). 
    # Adding new nodes with a different order will result into different trees

