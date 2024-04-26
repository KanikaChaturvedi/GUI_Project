class Node:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add_child(self, child_name: str):
        child_node = Node(child_name)
        self.children.append(child_node)
        return child_node

    def print(self):
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            print(f"{current_node.name}: ", end="")
            print(", ".join(child.name for child in current_node.children))
            queue.extend(current_node.children)

def merge(inp):
    root = Node("*")
    for path in inp:
        current_node = root
        for name in path[1:]:
            found = False
            for child in current_node.children:
                if child.name == name:
                    current_node = child
                    found = True
                    break
            if not found:
                current_node = current_node.add_child(name)
    return root

if __name__ == "__main__":
    root = merge([
        ["*", "a", "b", "car"],
        ["*", "a", "b", "e"],
        ["*", "a", "d", "b"],
        ["*", "a", "x"]
    ])

    root.print()
