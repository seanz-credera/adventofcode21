class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.visited = False
        self.children = []


with open("day12.txt") as file:
    file_content = file.readlines()
    file_content = [line.strip() for line in file_content]
    nodes = dict()
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
    for k, v in nodes.items():
        print(k, v)

    queue = ["start"]
    while len(queue) > 0:
        node = queue.pop()
        for connection in nodes[node]:
            queue.append(connection)
