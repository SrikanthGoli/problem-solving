# Binary Search Tree

class binarySearchTree(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def push(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = binarySearchTree(data)
                else:
                    self.left.push(data)
            else:
                if self.right is None:
                    self.right = binarySearchTree(data)
                else:
                    self.right.push(data)

        else:
            self.data = data

    def inorderTraversal(self, root):

        res = []

        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)

        return res

    def preOrderTraversal(self, root):

        res = []

        if root:
            res.append(root.data)
            res += self.preOrderTraversal(root.left)
            res += self.preOrderTraversal(root.right)

        return res

    def postOrderTraversal(self, root):

        res = []

        if root:
            res += self.postOrderTraversal(root.left)
            res += self.postOrderTraversal(root.right)
            res.append(root.data)

        return res


tree = binarySearchTree(55)
tree.push(50)
tree.push(40)
tree.push(60)
tree.push(30)
tree.push(70)
tree.push(35)
tree.push(80)
tree.push(23)
print(tree.postOrderTraversal(tree))
