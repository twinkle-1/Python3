from Node import DynamicNode


class Queue:
    def __init__(self, Node, max_items):
        self.Node = Node
        self.max_items = max_items
        self.head = None
        self.tail = None
        self.len = 0
        if not "next" in dir(Node('_')):
            raise Exception('Node Class must have next variable')

    def enqueue(self, node) -> None:
        if self.head is None:
            node = self.Node(node)
            self.head = node
            self.tail = node
            self.len += 1
        elif self.len < self.max_items:
            node = self.Node(node)
            if self.tail is None:
                self.head.next = node
                self.tail = node
            else:
                temp = self.tail
                self.tail.next = node
                self.tail = self.tail.next
            self.len += 1
        else:
            raise Exception("Queue Memory is Full")

    def dequeue(self):
        if self.len == 0:
            raise Exception("Queue Is empty")
        else:
            deleted_node = self.head
            self.head = self.head.next
            self.len -= 1
        return deleted_node

    def print_queue(self) -> None:
        current = self.head
        if self.len:
            while current.next is not None:
                print(current.data)
                current = current.next
            print(current.data)
        else:
            print("Queue is empty")

    def __len__(self):
        return self.len


if __name__ == "__main__":
    pass
    # Node = DynamicNode('next','data').getNode()
    # queue = Queue(Node, 7)
    # for x in range(1, 7):
    #     queue.enqueue(x)
    # for x in range(1, 7):
    #     print(queue.dequeue().data)
