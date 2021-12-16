from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    data = Path(args.infile).read_text().rstrip("\n")
    x = "D2FE28"
    b = bin(int(x, 16))[2:]

    i = 0
    vers = int(b[i:i+3], 2)
    print(vers)
    i += 3
    type_id = int(b[i:i+3], 2)
    print(type_id)
    i += 3

    if type_id == 4:

        groups = []
        while b[i] == "1":
            g = b[i+1:i+5]
            groups.append(g)
            i += 5
        g = b[i+1:i+5]
        groups.append(g)
        result = int("".join(groups), 2))
