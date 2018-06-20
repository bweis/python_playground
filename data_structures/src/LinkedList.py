from data_structures.src.ListNode import ListNode


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = ListNode(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count
