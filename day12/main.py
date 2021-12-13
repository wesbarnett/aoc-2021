from argparse import ArgumentParser
from collections import Counter, defaultdict
from pathlib import Path
import time


def traverse(graph, can_visit_cave_func):

    visited = Counter()

    def visit(node):

        if node == "end":
            return 1

        if node.islower():
            visited[node] += 1

        s = sum(visit(dst) for dst in graph[node] if can_visit_cave_func(visited, dst))

        if visited[node] > 0:
            visited[node] -= 1

        return s

    return visit("start")


def visited_small_cave_twice(visited):
    return visited.most_common()[0][1] == 2


def can_visit_cave(visited, dst):
    return dst != "start" and visited[dst] == 0


def can_visit_cave2(visited, dst):
    return dst != "start" and (
        (not visited_small_cave_twice(visited) and visited[dst] < 2) or
        (visited_small_cave_twice and visited[dst] < 1)
    )


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

    start = time.time()
    print(f"Result: {traverse(graph, can_visit_cave)}")
    end = time.time()
    print(f"Elapsed: {end - start:.3f}s")

    start = time.time()
    print(f"Result: {traverse(graph, can_visit_cave2)}")
    end = time.time()
    print(f"Elapsed: {end - start:.3f}s")
