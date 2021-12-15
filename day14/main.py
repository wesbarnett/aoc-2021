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
    for pair, ins in rules:
        new_pair_counts[pair[0]+ins] += pair_counts[pair]
        new_pair_counts[ins+pair[1]] += pair_counts[pair]
        new_pair_counts[pair] -= pair_counts[pair]
    return new_pair_counts


def run(steps, polymer_template, rules):
    pair_counts = init_pair_counts(polymer_template)

    for _ in range(steps):
        pair_counts = update_pair_counts(pair_counts, rules)

    return get_element_counts(pair_counts, polymer_template[0])


def get_element_counts(pair_counts, first_char):
    """
    Count each second element in a pair. By doing this we miss the first element of the
    polymer, so add 1 for it.
    """

    counts = Counter()
    for k, v in pair_counts.items():
        counts[k[1]] += v

    counts[first_char] += 1

    return counts


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument("-i", "--infile", required=False, type=Path, default=Path("input"))
    args = parser.parse_args()

    lines = Path(args.infile).read_text().rstrip("\n").split("\n")
    polymer_template = lines[0]
    rules = [rule.split(" -> ") for rule in lines[2:]]

    counts = run(10, polymer_template, rules)
    print(counts.most_common()[0][1]-counts.most_common()[-1][1])

    counts = run(40, polymer_template, rules)
    print(counts.most_common()[0][1]-counts.most_common()[-1][1])
