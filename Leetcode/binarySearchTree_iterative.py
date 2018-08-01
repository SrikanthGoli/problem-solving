
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

class binarySearchTree(object):

    def __init__(self, data = None):
        self.root = Node(data)

    def add(self, data):

        prev_node = None
        new_node = Node(data)
        curr_node = self.root

        if curr_node.data == None:
            self.root = new_node

        else:
            while curr_node != None:
                prev_node = curr_node
                if data < curr_node.data:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

            new_node.parent = prev_node

            if data < prev_node.data:
                prev_node.left = new_node
            else:
                prev_node.right = new_node

    def inorderTraversal(self, root):

        res = []

        if root != None:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)

        return res

    def preorderTraversal(self, root):

        res = []

        if root:
            res.append(root.data)
            res += self.preorderTraversal(root.left)
            res += self.preorderTraversal(root.right)

        return res

    def postorderTraversal(self, root):

        res = []

        if root:
            res += self.postorderTraversal(root.left)
            res += self.postorderTraversal(root.right)
            res.append(root.data)

        return res


tree = binarySearchTree()
tree.add(100)
tree.add(20)
tree.add(80)
tree.add(180)
tree.add(70)
tree.add(170)
tree.add(450)
tree.add(60)
tree.add(22)
print(tree.inorderTraversal(tree.root))
print(tree.preorderTraversal(tree.root))
print(tree.postorderTraversal(tree.root))