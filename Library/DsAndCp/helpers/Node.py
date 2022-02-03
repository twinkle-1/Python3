class Node:
    ownSlots = []

    def __init__(self, *args, **kwargs):
        if self.ownSlots:
            for element in self.ownSlots:
                self.__dict__.update(element)
        self.data = args[0]


class DynamicNode:
    def __init__(self, *args, **kwargs):
        checkDataFlag = False
        for arg in args:
            if arg == "data":
                checkDataFlag = True
            self.__dict__[arg] = None
        for krg in kwargs:
            if arg == "data":
                checkDataFlag = True
            self.__dict__[krg] = None
        if not checkDataFlag:
            raise NameError("'data' variable is not passed to save the data you need to pass the data variable")
        Node.ownSlots.append(self.__dict__)

    def getNode(self, *args, **kwargs):
        return Node


if __name__ == "__main__":
    pass
    # Node = DynamicNode('next','data').getNode()
    # print(Node(10).data)
    # print(Node(20).data)


