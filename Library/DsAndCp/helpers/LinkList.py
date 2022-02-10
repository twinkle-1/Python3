from Node import DynamicNode


class Linklist:

    def printLinklist(self, root):
        while root is not None:
            print("-> %s" % root.data, end="")
            root = root.next

    def itterateToEnd(self, node):
        tempCurrent = self.head
        while tempCurrent.next is not None:
            tempCurrent = tempCurrent.next
        return tempCurrent

    def itterateToK(self, node, K):
        index = 0
        tempCurrent = node
        while index != K - 1:
            tempCurrent = tempCurrent.next
            index += 1
        return tempCurrent


class SinglyLinkList(Linklist):
    def __init__(self, data=None):
        self.head = None
        self.val = 0
        self.linen = 0

    def addNodeAtK(self, node, position):
        if position <= self.linen:
            if position < self.linen:
                current = self.itterateToK(self.head, position)
                nextOfNext = current.next
                current.next = node
                node.next = nextOfNext
                self.linen += 1
                return node
            else:
                if position == 0:
                    return self.addNoteAtHead(node)
                else:
                    return self.addNodeAtEnd(node)
        else:
            raise IndexError("Wrong Position To insert the element")

    def addNodeAtEnd(self, node, endElement=False):
        if endElement:
            self.linen += 1
            endElement.next = node
            return endElement.next
        else:
            self.addNodeAtEnd(node, self.itterateToEnd(self.head))

    def addNoteAtHead(self, node):
        if self.linen > 0:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        self.linen += 1
        return self.head

    def addNode(self, node, position=False, previousElement=False):
        if previousElement and self.linen > 0:
            '''
                End Element Case
            '''
            return self.addNodeAtEnd(node, previousElement)
        elif position and self.linen > 0:
            '''
                K position Case
            '''
            return self.addNodeAtK(node, position)
        else:
            '''
                First Case
            '''
            return self.addNoteAtHead(node)

    def delNodeAtK(self):
        ...

    def delNodeAtEnd(self):
        ...

    def delNoteAtHead(self):
        ...

    def delNode(self, position=False):
        ...

    def printLinklist(self):
        super(SinglyLinkList, self).printLinklist(self.head)

    def __len__(self):
        return self.linen


Node = DynamicNode('next', 'data').getNode()


def createSinglyRange(llObject,ittretableObj):
    linkList = llObject
    linkList.head = Node(ittretableObj[0])
    currentNode = linkList.head
    linkList.linen += 1
    for index in ittretableObj[1:]:
        currentNode = linkList.addNode(node=Node(index), previousElement=currentNode)
    return linkList


def link_list(name, data=False):
    method = "%sLinkList" % name.capitalize()
    try:
        llObject = eval(method)()
        if data:
            eval("create%sRange" % name.capitalize())(llObject, data)
        return llObject
    except Exception as e:
        return e


if __name__ == "__main__":
    boom = link_list('singly',[1,2,3,4,5,6,7,8])
    boom.printLinklist()
