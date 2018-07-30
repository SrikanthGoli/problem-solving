
# Binary Search Tree
class Node(object):

    def __init__(self, data = None):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class binarySearchTree(object):

    def __init__(self):
        self.root = Node()

    def push(self, data):

        new_node = Node(data)
        curr_node = self.root

        if curr_node.data == None:
            curr_node.data = data

        else:
            while curr_node.left != None and curr_node.right != None:
                if curr_node.data > new_node.data:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

            if curr_node.data > data:
                curr_node.left = new_node
                curr_node.left.parent = curr_node
            else:
                curr_node.right = new_node
                curr_node.right.parent = curr_node


    def inorderTraversal(self, root):

        res = []

        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res += self.inorderTraversal(root.right)
            print(res)

        return res



tree = binarySearchTree()
tree.push(50)
tree.push(40)
tree.push(60)
tree.push(30)
tree.push(70)
tree.push(35)
tree.push(80)
tree.push(23)
print(tree.inorderTraversal(tree.root))