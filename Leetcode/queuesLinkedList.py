
# Implementing Queues using linked list

class Node(object):

    def __init__(self, data = None):

        self.data = data
        self.next = None

class queue(object):

    def __init__(self, data):

        self.root = Node(data)

    def enQueue(self, data):

        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    def deQueue(self):

        prev_node = self.root
        curr_node = prev_node.next

        if prev_node.next == None:
            self.root = None

        else:
            while curr_node.next != None:
                prev_node = curr_node
                curr_node = curr_node.next

            prev_node.next = None

    def diplay(self):

        res = []
        curr_node = self.root

        while curr_node != None:
            res.append(curr_node.data)
            curr_node = curr_node.next

        return res
