from argparse import ArgumentParser
from pathlib import Path
from statistics import median


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
                return points[x], None
        elif x in pairs.values():
            stack.append(x)
        else:
            raise ValueError("Unexpected character")

    return 0, stack


def autocomplete(line):

    pairs = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    score = 0
    while line:
        score *= 5
        score += points[pairs[line.pop()]]

    return score


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    score = 0
    incomplete = []
    for line in lines:
        result, stack = find_first_incorrect_score(line)
        score += result
        if result == 0:
            incomplete.append(stack)

    print(score)

    print(median([autocomplete(line) for line in incomplete]))
