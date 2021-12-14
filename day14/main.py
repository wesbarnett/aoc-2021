from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return f"Node(val={self.val})"


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
    pair_insertion_rules = lines[2:]

    head = create_starting_polymer(polymer_template)

    for _ in range(10):
        insert_elements(head, pair_insertion_rules)

    counter = Counter()
    node = head
    while node:
        counter[node.val] += 1
        node = node.next

    print(counter.most_common()[0][1] - counter.most_common()[-1][1])
