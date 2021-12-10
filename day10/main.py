from argparse import ArgumentParser
from pathlib import Path


def find_first_incorrect_score(line):

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<"
    }

    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }

    stack = []
    for x in line:
        if x in pairs.keys():
            if stack[-1] == pairs[x]:
                stack.pop()
            else:
                return points[x]
        elif x in pairs.values():
            stack.append(x)
        else:
            raise ValueError("Unexpected character")

    return 0


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    print(sum(find_first_incorrect_score(line) for line in lines))
