class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
    def insert(self, node):
        if self.value > node.value:
            if self.left is None:
                self.left = node
            else:
                self.left.insert(node)

        elif self.value < node.value:
            if self.right is None:
                self.right = node
                node.parent = self
            else:
                self.right.insert(node)

    def search(self, value,d):
        if self.value > value:
            if self.left is not None:
                d[self.left.value] = value - self.left.value if self.left.value < value else self.left.value - value
                return self.left.search(value,d)
        else:
            if self.right is not None:
                d[self.right.value] = value - self.right.value if self.right.value < value else self.right.value - value
                return self.right.search(value,d)
        return d
 
 
class BST:
    def __init__(self):
        self.root = None
 
    def add(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert(new_node)
 
    def search(self, value):
        if self.root is not None:
            return self.root.search(value,{})
 
 
bst = BST()
family_diet = list(map(int,input('Enter the diet of family members: ').split()))

for diet in family_diet:
    bst.add(diet)

new_diet = int(input('Enter the diet of the new member: '))

d = bst.search(new_diet)

_min = 2 ** 64 - 1
key, val = None, None

for i,j in d.items():
    if(d[i] < _min):
        _min = d[i]
        key, val = i,j

if(val == 0):
    print('Same value Found')
else:
    print('The closest value is: ', key)
