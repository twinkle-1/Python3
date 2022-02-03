from Node import DynamicNode
class Stack:
    def __init__(self, Node, max_items):
        self.head = None
        self.Node = Node
        self.max_items = max_items
        self.len = 0
        if not "next" in dir(Node('_')):
            raise Exception('Node Class must have next variable')

    def push(self, node):
        if self.head is None:
            self.head = self.Node(node)
            self.len += 1
        elif self.len < self.max_items:
            current = self.head
            self.head = self.Node(node)
            self.head.next = current
            self.len += 1
        else:
            raise Exception("Stack Memory is Full")

    def pop(self):
        if self.len == 0:
            raise Exception("Stack Is empty")
        else:
            self.len -= 1
            deleted_node = self.head
            self.head = self.head.next
            return deleted_node

    def print_stack(self):
        current = self.head
        if self.len:
            while current.next is not None:
                print(current.data)
                current = current.next
            print(current.data)
        else:
            print('Stack is empty')

    def __len__(self):
        return self.len


if __name__ == "__main__":
    pass
    # Node = DynamicNode('next', 'data').getNode()
