








class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # while node and node.next_node:
        #     node = node.next_node
        #     self.add_to_head(node.value)
        while self.head:
            if node.next_node:
                return self.reverse_list(node.next_node, node.value)
            else:
                return self.add_to_head(node.value)
                #return self.add_to_head(node.value)
        # if node:
        #     node.set_next(prev)



        # while current:
        #     next = current.next_node
        #     return reverse_list(node)
        # else:
        #     return self.value












llist = LinkedList()


llist.add_to_head(1)
llist.add_to_head(2)
llist.add_to_head(3)
llist.add_to_head(4)
llist.add_to_head(5)
print(llist.head.value == 5)
llist.reverse_list(llist.head, None)
print(llist.head.value == 1)
print(llist.head.get_next().value == 2)
print(llist.head.get_next().get_next().value == 3)


print(llist.head.get_next().value)