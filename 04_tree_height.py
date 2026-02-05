# Tree Blueprint   
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

# Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)

# Tree Height Code
def height_finder(a):
    if a == None:
        return 0
    else:
        ldepth = height_finder(a.left)
        rdepth = height_finder(a.right)

        if ldepth > rdepth:
            return ldepth + 1
        else:
            return rdepth + 1

print(height_finder(root))