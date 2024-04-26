## Save this file as merge.py. Run `python3 merge.py` to see the output.


# if __name__ == "__main__":
#     root = merge([
#         ["*", "a", "b", "car"],
#         ["*", "a", "b", "e"],
#         ["*", "a", "d", "b"],
#         ["*", "a", "x"]
#     ])

#     root.print()

from typing import List
class Node:
    def __init__(self, nodeName: str):
        self.nodeName = nodeName
        # self.subNodes= {}; 
        self.subNodes = []

    def addSubNode(self, subNodeName: str):
        subNode = Node(subNodeName)
        self.subNodes.append(subNode)
        return subNode

    def print(self):
         # Do a BFS of the tree to print
        queue = [self]   
        while queue:
            curNode = queue.pop(0)

            nodeName = curNode.nodeName
            print(nodeName + " -> ", end=" ")
            subnodeNames = [subNode.nodeName for subNode in curNode.subNodes]
            print(" , ".join(subnodeNames))

            queue.extend(curNode.subNodes)

def merge(inp):
    # Merge the lists into tree here and return root Node
    root = Node("*")
    for itlist in inp:
        curNode = root
        # iterate from first element and skip first element since its is * .
        for name in itlist[0:]:
            if name == "*":
                continue
            flag = False
            for subNode in curNode.subNodes:
                if subNode.nodeName == name:
                    curNode = subNode
                    flag = True
                    break
            if not flag:
                curNode = curNode.addSubNode(name)
    return root

if __name__ == "__main__":
    root = merge([
        ["*", "a", "b", "car"],
        ["*", "a", "b", "e"],
        ["*", "a", "d", "b"],
        ["*", "a", "x"]
    ])

    root.print()

