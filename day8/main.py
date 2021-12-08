from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path


if __name__ == "__main__":

    digits = {
        0: "abcefg",
        1: "cf",
        2: "acdeg",
        3: "acdfg",
        4: "bcdf",
        5: "abdfg",
        6: "abdefg",
        7: "acf",
        8: "abcdefg",
        9: "abcdfg"
    }

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    lengths = defaultdict(list)
    for k, v in digits.items():
        lengths[len(v)].append(k)

    unique_length = []
    for k, v in lengths.items():
        if len(v) == 1:
            unique_length.append(k)

    count = 0
    for line in lines:
        signal, output = line.split(" | ")
        for x in output.split():
            if len(x) in unique_length:
                count += 1

    print(count)
