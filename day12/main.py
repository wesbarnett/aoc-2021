from argparse import ArgumentParser
from collections import Counter, defaultdict
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


def visited_small_cave_twice(visited):
    return visited.most_common()[0][1] == 2


def can_visit_cave(visited, dst):
    return dst != "start" and (not visited_small_cave_twice(visited) and visited[dst] < 2) or (visited_small_cave_twice and visited[dst] < 1)


def traverse2(node, graph):

    visited = Counter()

    def visit(node):

        if node == "end":
            return 1

        if node.islower():
            visited[node] += 1

        s = 0
        for dst in graph[node]:
            if can_visit_cave(visited, dst):
                s += visit(dst)

        if node.islower() and visited[node] > 0:
            visited[node] -= 1

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

    print(graph)
    print(traverse("start", graph))
    print(traverse2("start", graph))
