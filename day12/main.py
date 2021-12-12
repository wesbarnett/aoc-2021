from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path


def traverse(node, graph):

    visited = set(["start"])

    def visit(node):

        if node == "end":
            return 1

        if node.islower():
            visited.add(node)

        s = 0
        for dst in graph[node]:
            if dst not in visited:
                s += visit(dst)

        if node in visited:
            visited.remove(node)

        return s

    result = visit(node)
    return result


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    graph = defaultdict(set)

    for line in lines:
        src, dst = line.split("-")
        graph[src].add(dst)
        if src != "start" and dst != "end":
            graph[dst].add(src)

    print(traverse("start", graph))
