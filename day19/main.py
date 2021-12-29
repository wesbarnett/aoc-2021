from argparse import ArgumentParser
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path

def search(scanners, j, offset):
    for k in range(len(scanners[j])):
        x0, y0, z0 = scanners[j][k]
        for i in range(len(scanners.keys())):
            if i != j:
                for s in product([-1, 1], repeat=3):
                    for d in permutations(range(3)):
                        for p in scanners[i]:
                            x1, y1, z1 = s[0]*p[d[0]], s[1]*p[d[1]], s[2]*p[d[2]]
                            dx, dy, dz = x0 - x1, y0 - y1, z0 - z1
                            beacons = []
                            for p in scanners[i]:
                                beacon = s[0]*p[d[0]] + dx, s[1]*p[d[1]] + dy, s[2]*p[d[2]] + dz
                                if beacon in scanners[j]:
                                    beacons.append(beacon)
                            if len(beacons) >= 12:
#                               for beacon in beacons:
#                                   all_beacons.add(beacon)
                                offset[(j, i)] = tuple((dx, dy, dz))
                                return
    

if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")

    scanners = defaultdict(list)
    i = -1
    for line in lines:
        if line.startswith("---"):
            i += 1
        elif line:
            scanners[i].append(tuple(map(int, line.split(","))))

    offset = {}

    for j in range(5):
        search(scanners, j, offset)

    print(offset)
#   print(all_beacons)
