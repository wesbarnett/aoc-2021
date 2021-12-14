from argparse import ArgumentParser
from collections import Counter
from pathlib import Path


def init_pair_counts(template):

    pair_counts = Counter()
    for i in range(len(polymer_template[:-1])):
        pair_counts[polymer_template[i:i+2]] += 1

    return pair_counts


def update_pair_counts(pair_counts, rules):
    """
    When an element is inserted between a pair, that pair is eliminated and the new
    pairs are added.
    """

    # Keep a separate copy of the counter because the rules are applied at the same time
    new_pair_counts = Counter(pair_counts)
    for rule in rules:
        pair, ins = rule.split(" -> ")
        if pair_counts[pair] > 0:
            new_pair_counts[pair[0]+ins] += pair_counts[pair]
            new_pair_counts[ins+pair[1]] += pair_counts[pair]
            new_pair_counts[pair] -= pair_counts[pair]
    return Counter(new_pair_counts)


def run(steps, polymer_template, rules):
    pair_counts = init_pair_counts(polymer_template)

    for _ in range(steps):
        pair_counts = update_pair_counts(pair_counts, rules)

    return get_element_counts(pair_counts)


def get_element_counts(pair_counts):
    """
    Count each starting element and ending element for each pair. These should be
    exactly the same numbers for each element except for the starting pair and the
    ending pair (which will be off by one). Thus we take the max for each element from
    those two counts.
    """

    counts1 = Counter()
    counts2 = Counter()
    for k, v in pair_counts.items():
        counts1[k[0]] += v
        counts2[k[1]] += v

    counts = Counter()
    for k in counts1.keys():
        counts[k] = max(counts1[k], counts2[k])

    return counts


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")
    polymer_template = lines[0]
    rules = lines[2:]

    counts = run(10, polymer_template, rules)
    print(counts.most_common()[0][1]-counts.most_common()[-1][1])

    counts = run(40, polymer_template, rules)
    print(counts.most_common()[0][1]-counts.most_common()[-1][1])
