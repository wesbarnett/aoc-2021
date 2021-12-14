from argparse import ArgumentParser
from pathlib import Path


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        if self.next:
            return f"Node(val={self.val}, next={self.next.val})"
        else:
            return f"Node(val={self.val}, next=None)"


def create_starting_polymer(polymer_template):
    head = Node(polymer_template[0])
    node = head
    for i in range(1, len(polymer_template)):
        node.next = Node(polymer_template[i])
        node = node.next
    return head


def insert_elements(head, rules):

    node = head
    while node:
        for rule in rules:
            pair, ins = rule.split(" -> ")
            new_node = Node(ins)
            if node.val == pair[0] and node.next and node.next.val == pair[1]:
                new_node.next, node.next = node.next, new_node
                node = new_node
                break
        node = node.next


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")
    polymer_template = lines[0]
    pair_insertion_rules = lines[3:]

    head = create_starting_polymer(polymer_template)

    node = head
    while node:
        print(node)
        node = node.next

    insert_elements(head, pair_insertion_rules)

    node = head
    while node:
        print(node)
        node = node.next
