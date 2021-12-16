from collections import defaultdict, Counter


def check_small_caves(path):
    count = Counter(path)
    for cave, times_visited in count.items():
        if cave.islower() and times_visited == 2:
            return False
    return True


filename = "day12.txt"
debug = "AoC-John/Day12/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    nodes = defaultdict(list)
    for line in file_content:
        n = line.split("-")
        if n[0] in nodes:
            nodes[n[0]].append(n[1])
        else:
            nodes[n[0]] = [n[1]]
        if n[1] in nodes:
            nodes[n[1]].append(n[0])
        else:
            nodes[n[1]] = [n[0]]
    for node, connections in nodes.items():
        print(node, connections)

    # Keep items in stack as lists that keep track of paths taken
    # See what's been visited by checking if they are in the path or not
    queue = [["start"]]
    paths = []
    while len(queue) > 0:
        node_path = queue.pop(0)
        if node_path[-1] == "end":
            paths.append(node_path)
            continue
        for connection in nodes[node_path[-1]]:
            if connection != "start" and (
                connection not in node_path
                or check_small_caves(node_path)
                or connection.isupper()
            ):
                queue.append(node_path + [connection])
    for path in paths:
        print(path)

    print(f"\nNumber of paths: {len(paths)}")
