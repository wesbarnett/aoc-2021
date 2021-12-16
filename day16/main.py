from argparse import ArgumentParser
from pathlib import Path


def calc_literal(b, i):
    groups = []
    while b[i] == "1":
        i, g = i+5, b[i+1:i+5]
        groups.append(g)
    i, g = i+5, b[i+1:i+5]
    groups.append(g)
    return i, int("".join(groups), 2)


def next_val(b, i, amt=1):
    return i+amt, int(b[i:i+amt], 2)


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    x = Path(args.infile).read_text().rstrip("\n")
    x = "D2FE28"
    x = "38006F45291200"
    # x = "EE00D40C823060"
    # x = "8A004A801A8002F478"
    # x = "620080001611562C8802118E34"
    # x = "C0015000016115A2E0802F182340"
    # x = "A0016C880162017C3686B18A3D4780"
    print(x)
    b = format(int(x, 16), f"0>{len(x)*4}b")

    total_vers = 0

    def run(b):

        global total_vers
        print(b)

        i, vers = next_val(b, 0, 3)
        total_vers += vers
        print(f"vers = {vers}")

        i, type_id = next_val(b, i, 3)
        print(f"type id = {type_id}")

        if type_id == 4:
            print("calc literal")
            i, val = calc_literal(b, i)
            print(f"val = {val}")
            return i, val

        else:

            print("operator packet")

            i, length_type_id = i+1, b[i]

            if length_type_id == "0":

                i, packet_length = next_val(b, i, 15)
                print(f"packet length = {packet_length}")

                length = 0
                i += length
                while length < packet_length:
                    j, val = run(b[i:])
                    i += j
                    length += j
                    print(f"length = {length}")

            else:
                i, num_packets = next_val(b, i, 11)
                print(f"num packets = {num_packets}")
                for p in range(num_packets):
                    print(f"packet {p}")
                    j, val = run(b[i:])
                    i += j
        print(b)

    run(b)
    print(total_vers)
