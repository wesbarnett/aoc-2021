from argparse import ArgumentParser
from pathlib import Path

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    data = Path(args.infile).read_text().rstrip("\n")
    # x = "D2FE28"
    x = "38006F45291200"
    b = format(int(x, 16), f"0>{len(x)*4}b")

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
        result = int("".join(groups), 2)
        print(result)
    else:
        length_type_id = b[i]
        if length_type_id == "0":
            i += 1
            packet_length = int(b[i:i+15], 2)
            print(packet_length)
        else:
            pass
