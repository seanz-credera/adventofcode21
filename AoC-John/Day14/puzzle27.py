from collections import Counter


def process_rules_list(rules_list):
    rules = dict()
    for rule in rules_list:
        separated = rule.split("->")
        pattern, inserted = separated[0].strip(), separated[1].strip()
        rules[pattern] = inserted
    return rules


# Return the element at index with the correct element inserted after it according to rule
# Each elt is a "first" elt in a pair, just focus on those
def insert_element(rules, template, index):
    pair = template[index] + template[index + 1]
    if rules.get(pair):
        return template[index] + rules[pair]
    return template[index]


NUM_STEPS = 10

debug_filename = "AoC-John/Day14/day14.txt"
filename = "day14.txt"

with open(filename) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content if len(line.strip()) > 0]
    template, rules_list = file_content[0], file_content[1:]
    print(f"Template: {template}")
    rules = process_rules_list(rules_list)
    for step in range(NUM_STEPS):
        new_template = ""
        for index in range(len(template) - 1):
            new_template += insert_element(rules, template, index)
        # Every element is the 'first' of a pair except the last, so it wasn't accounted for
        new_template += template[-1]
        template = new_template
        print(f"Step {step + 1} complete.")
        # print(f"After step {step + 1}: {template}")
    elements = list(template)
    count = Counter(elements)
    ordered_count = count.most_common()
    max_elt = ordered_count[0]
    min_elt = ordered_count[-1]

    print(f"Most common element, count: {max_elt[0]}, {max_elt[1]}")
    print(f"Least common element, count: {min_elt[0]}, {min_elt[1]}")
    print(f"Final answer: {max_elt[1] - min_elt[1]}")
