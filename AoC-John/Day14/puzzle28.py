from collections import Counter, defaultdict
from typing import List

# Get pair counts from initial template
def get_pair_counts(template: str) -> defaultdict:
    counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        counts[pair] += 1
    return counts


# From pair_counts, get the individual element counts
def get_element_counts(pair_counts: defaultdict) -> defaultdict:
    element_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        e1, e2 = pair[0], pair[1]
        element_counts[e1] += count
    return element_counts


# Write input rules to dict of pair:inserted char
def process_rules_list(rules_list: List[str]) -> dict:
    rules = dict()
    for rule in rules_list:
        separated = rule.split("->")
        pattern, inserted = separated[0].strip(), separated[1].strip()
        rules[pattern] = inserted
    return rules


# Update pair counts based on which char rules say to insert
def update_pair_counts(pair_counts: defaultdict, rules: dict) -> defaultdict:
    new_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        inserted = rules[pair]
        new_p1 = pair[0] + inserted
        new_p2 = inserted + pair[1]
        new_counts[new_p1] += count
        new_counts[new_p2] += count
    return new_counts


NUM_STEPS = 40

debug_filename = "AoC-John/Day14/day14.txt"
filename = "day14.txt"

with open(debug_filename) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content if len(line.strip()) > 0]
    template, rules_list = file_content[0], file_content[1:]
    print(f"Template: {template}")
    rules = process_rules_list(rules_list)
    pair_counts = get_pair_counts(template)
    for step in range(NUM_STEPS):
        pair_counts = update_pair_counts(pair_counts, rules)
        print(f"Step {step + 1} complete.")

    element_counts = get_element_counts(pair_counts)
    max_key = max(element_counts, key=element_counts.get)
    min_key = min(element_counts, key=element_counts.get)
    print(f"Most common element, count: {max_key}, {element_counts[max_key]}")
    print(f"Least common element, count: {min_key}, {element_counts[min_key]}")
    print(f"Final answer: {element_counts[max_key] - element_counts[min_key]}")
