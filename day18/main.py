from argparse import ArgumentParser
from pathlib import Path
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
    exploded = False

    def helper(node, level=0):

        nonlocal prev_node
        nonlocal right_val
        nonlocal exploded

        if node.left is not None and node.right is not None and level == 4:
            if node.left.val is not None and node.right.val is not None and not exploded:
                left, right = node.left.val, node.right.val
                node.val = 0
                node.left = None
                node.right = None
                node.exploded = True
                if prev_node is not None:
                    prev_node.val += left
                right_val = right
                exploded = True

        if right_val is not None and node.val is not None and not node.exploded:
            node.val += right_val
            right_val = None
            return True

        if node.val is not None:
            prev_node = node

        if node.left is not None:
            status = helper(node.left, level+1)
            if status:
                return status

        if node.right is not None:
            status = helper(node.right, level+1)
            if status:
                return status

        return False

    helper(root)
    reset_exploded(root)


def split(root):

    def helper(node):

        if node.left is None and node.right is None:
            if node.val > 9:
                val = node.val
                node.left = Node(math.floor(val / 2))
                node.right = Node(math.ceil(val / 2))
                return True

        if node.left is not None:
            status = helper(node.left)
            if status:
                return True

        if node.right is not None:
            status = helper(node.right)
            if status:
                return True

        return False

    helper(root)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

#   lines = [
#       "[[[[4,3],4],4],[7,[[8,4],9]]]",
#       "[1,1]"
#   ]
    num1 = eval(lines[0])

    for line in lines[1:]:

        num2 = eval(line)
        A = add(num1, num2)
        root = create_tree(A)
        tree = print_tree(root)
        new_tree = None

        while tree != new_tree:
            tree = new_tree

            tree2 = tree
            new_tree2 = None
            while tree2 != new_tree2:
                tree2 = new_tree2
                explode(root)
                new_tree2 = print_tree(root)

            split(root)
            new_tree = print_tree(root)

        num1 = new_tree

    print(new_tree)
