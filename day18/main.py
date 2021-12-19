
class Node:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val


def add(x, y):
    return [x] + [y]


def create_tree(A):

    def helper(A, node):

        left, right = A[0], A[1]

        if isinstance(left, list):
            node.left = Node()
            helper(left, node.left)
        else:
            node.left = Node(left)

        if isinstance(right, list):
            node.right = Node()
            helper(right, node.right)
        else:
            node.right = Node(right)

    root = Node()
    helper(A, root)
    return root


def traverse(node):

    if node.left is None and node.right is None:
        print(node.val)

    if node.left is not None:
        traverse(node.left)

    if node.right is not None:
        traverse(node.right)


def explode(root):

    def helper(node, level=0):

        if node.left is not None and node.right is not None:
            if node.left.val is not None and node.right.val is not None:
                left, right = node.left.val, node.right.val
                node.val = 0
                node.left = None
                node.right = None
                return left, right

        left = right = None
        if node.left is not None:
            left = helper(node.left, level+1)

        if node.right is not None:
            right = helper(node.right, level+1)

        if left is not None:
            return left
        else:
            return right

    return helper(root)


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

    A = eval("[[[[[9,8],1],2],3],4]")
    # A = eval("[7,[6,[5,[4,[3,2]]]]]")
    # A = eval("[[6,[5,[4,[3,2]]]],1]")

    root = create_tree(A)

    traverse(root)

    print(explode(root))

    traverse(root)
