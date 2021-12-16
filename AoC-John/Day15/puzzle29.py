from collections import defaultdict
from typing import List


def dijkstra(net, s, t):
    # sanity check
    if s == t:
        return "The start and terminal nodes are the same. Minimum distance is 0."
    if s not in net:  # python2: if net.has_key(s)==False:
        return "There is no start node called " + str(s) + "."
    if t not in net:  # python2: if net.has_key(t)==False:
        return "There is no terminal node called " + str(t) + "."
    # create a labels dictionary
    labels = {}
    # record whether a label was updated
    order = {}
    # populate an initial labels dictionary
    for i in net.keys():
        if i == s:
            labels[i] = 0  # shortest distance form s to s is 0
        else:
            labels[i] = float("inf")  # initial labels are infinity
    from copy import copy

    drop1 = copy(labels)  # used for looping
    ## begin algorithm
    while len(drop1) > 0:
        # find the key with the lowest label
        minNode = min(
            drop1, key=drop1.get
        )  # minNode is the node with the smallest label
        # update labels for nodes that are connected to minNode
        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        del drop1[minNode]  # once a node has been visited, it's excluded from drop1
    ## end algorithm
    # print shortest path
    temp = copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if temp in order:
            temp = order[temp]  # if order.has_key(temp): temp = order[temp]
        else:
            return "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath) - 1, -1, -1):
        path.append(rpath[j])
    return f"The shortest path from {s} to {t} is {str(path)}. Minimum distance is {str(labels[t])}."


class mylist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


class Node:
    def __init__(self, value: int, row: int, col: int) -> None:
        self.value = value
        self.row = row
        self.col = col
        self.connections = mylist()
        self.visited = False

    def __eq__(self, other: object) -> bool:
        return (self.row == other.row) and (self.col == other.col)

    def __str__(self) -> str:
        return f"{self.value} @ ({self.row}, {self.col})"


def get_connections(nodes: List[int], row: int, col: int) -> List[Node]:
    connections = dict()
    try:
        connections[(row, col - 1)] = nodes[row][col - 1]
    except:
        pass
    try:
        connections[(row, col + 1)] = nodes[row][col + 1]
    except:
        pass
    try:
        connections[(row - 1, col)] = nodes[row - 1][col]
    except:
        pass
    try:
        connections[(row + 1, col)] = nodes[row + 1][col]
    except:
        pass
    return connections


filename = "day15.txt"
debug = "AoC-John/Day15/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = mylist(line.strip() for line in file_content)
    nodes_input = mylist()
    for line in file_content:
        nodes_input.append(mylist(int(num) for num in list(line)))

    nodes = defaultdict(dict)
    for row in range(len(nodes_input)):
        for col in range(len(nodes_input[0])):
            nodes[(row, col)] = get_connections(nodes_input, row, col)

    for node in nodes:
        if (0, 0) in nodes[node]:
            del nodes[node][(0, 0)]

    print(dijkstra(nodes, (0, 0), (len(nodes_input) - 1, len(nodes_input) - 1)))
