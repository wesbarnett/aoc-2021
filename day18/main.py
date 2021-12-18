
class Node:

    def __init__(self):
        self.left = None
        self.right = None


def add(x, y):
    return [x] + [y]


def create_tree(A, node):

    left, right = A[0], A[1]
    if isinstance(left, list):
        node.left = Node()
        create_tree(left, node.left)
    else:
        node.left = left
    if isinstance(right, list):
        node.right = Node()
        create_tree(right, node.right)
    else:
        node.right = right


def traverse(node, level=0):

    if isinstance(node.left, Node):
        traverse(node.left, level+1)
    else:
        print(node.left)

    if isinstance(node.right, Node):
        traverse(node.right, level+1)
    else:
        print(node.right)


if __name__ == "__main__":

    num1 = eval("[1,2]")
    num2 = eval("[[3,4],5]")
    # print(add(num1, num2))

    A = eval("[[[[[9,8],1],2],3],4]")
    # A = eval("[7,[6,[5,[4,[3,2]]]]]")
    # A = eval("[[6,[5,[4,[3,2]]]],1]")

    root = Node()
    create_tree(A, root)

    traverse(root)
