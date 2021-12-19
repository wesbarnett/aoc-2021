
from collections import deque

class Node:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.up = None


def add(x, y):
    return [x] + [y]


def create_tree(A, node):

    left, right = A[0], A[1]
    if isinstance(left, list):
        node.left = Node()
        node.left.up = node
        create_tree(left, node.left)
    else:
        node.left = left
    if isinstance(right, list):
        node.right = Node()
        node.right.up = node
        create_tree(right, node.right)
    else:
        node.right = right


def traverse(node, level=0):

    if isinstance(node.left, Node):
        traverse(node.left, level+1)
    if isinstance(node.right, Node):
        traverse(node.right, level+1)
    print(node.left, node.right)


def bfs(root):

    stack = [root.left, root.right]

    level = 0
    while stack:
        print(f"level = {level}")
        next_stack = []
        for x in stack:
            if isinstance(x, Node):
                next_stack.append(x.left)
                next_stack.append(x.right)
        if level == 4:
            print(stack)
        stack = next_stack
        level += 1


def update(node, level=0):

    if level == 4:
        up = node.up
        while not isinstance(up.right, int):
            print(up.right)
            up = up.up
        if isinstance(up.right, int):
            node.up.right += node.right
        else:
            node.up.right = node.right
        if isinstance(node.up.left, int):
            node.up.left += node.left
        else:
            node.up.left = node.left

    if isinstance(node.left, Node):
        update(node.left, level+1)

    if isinstance(node.right, Node):
        update(node.right, level+1)


if __name__ == "__main__":

    num1 = eval("[1,2]")
    num2 = eval("[[3,4],5]")
    # print(add(num1, num2))

    A = "[[[[[9,8],1],2],3],4]"
    #A = "[7,[6,[5,[4,[3,2]]]]]"
    #A = "[[6,[5,[4,[3,2]]]],1]"
    values = deque([])
    levels = deque([])
    level = -1
    for x in A:
        try:
            values.append(int(x))
            levels.append(level)
        except ValueError:
            if x == "[":
                level += 1
            elif x == "]":
                level -= 1

    print(values)
    print(levels)

    val1 = values.popleft()
    lev1 = levels.popleft()

    val2 = values.popleft()
    lev2 = levels.popleft()

    new_levels = deque([])
    new_values = deque([])

    if lev1 == 4 and lev2 == 4:
        if len(new_levels) == 0:
            new_values.append(0)
            new_levels.append(lev1)
            lev2 = 

        new_levels.append(lev1)

    else:
        new_levels.append(lev1)
        lev1 = lev2
        lev2 = levels.popleft()

        new_values.append(val1)
        val1 = val2
        val2 = values.popleft()


    for i in range(1, len(levels)):
        if values[i-1] == 4 and values[i] == 4:
            values[:i] + [0] + values[i+1:]
            levels[:i] + [3, 3] + levels


#   root = Node()
#   create_tree(A, root)

#   # traverse(root)
#   # bfs(root)
#   update(root)
#   print()

#   traverse(root)
