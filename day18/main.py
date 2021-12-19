import math


class Node:

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
        self.exploded = False


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


def print_tree(root):

    def helper(node):

        if node.left is None and node.right is None:
            return node.val

        if node.left is not None:
            left = helper(node.left)

        if node.right is not None:
            right = helper(node.right)

        return [left, right]

    return helper(root)


def traverse(node):

    if node.left is None and node.right is None:
        print(node.val)

    if node.left is not None:
        traverse(node.left)

    if node.right is not None:
        traverse(node.right)


def reset_exploded(node):

    def helper(node):

        node.exploded = False

        if node.left is not None:
            helper(node.left)

        if node.right is not None:
            helper(node.right)

    helper(node)


def explode(root):

    prev_node = None
    right_val = None

    def helper(node, level=0):

        nonlocal prev_node
        nonlocal right_val

        if node.left is not None and node.right is not None and level == 4:
            if node.left.val is not None and node.right.val is not None:
                left, right = node.left.val, node.right.val
                node.val = 0
                node.left = None
                node.right = None
                node.exploded = True
                if prev_node is not None:
                    prev_node.val += left
                right_val = right

        if right_val is not None and node.val is not None and not node.exploded:
            node.val += right_val
            right_val = None

        if node.val is not None:
            prev_node = node

        if node.left is not None:
            helper(node.left, level+1)

        if node.right is not None:
            helper(node.right, level+1)

    helper(root)
    reset_exploded(root)


def split(root):

    def helper(node):

        if node.left is None and node.right is None:
            if node.val > 9:
                val = node.val
                node.left = Node(math.floor(val / 2))
                node.right = Node(math.ceil(val / 2))

        if node.left is not None:
            helper(node.left)

        if node.right is not None:
            helper(node.right)

    helper(root)


if __name__ == "__main__":

    num1 = eval("[1,2]")
    num2 = eval("[[3,4],5]")
    # print(add(num1, num2))

    A = eval("[[[[[9,8],1],2],3],4]")
    # A = eval("[7,[6,[5,[4,[3,2]]]]]")
    #A = eval("[[6,[5,[4,[3,2]]]],1]")
    #A = eval("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]")

#   root = create_tree(A)
#   print(print_tree(root))

#   explode(root)
#   print(print_tree(root))

    num1 = eval("[[[[4,3],4],4],[7,[[8,4],9]]]")
    num2 = eval("[1,1]")

    A = add(num1, num2)

    root = create_tree(A)
    print(print_tree(root))

    explode(root)
    print(print_tree(root))

    split(root)
    print(print_tree(root))

    explode(root)
    print(print_tree(root))
