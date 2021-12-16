from collections import defaultdict
from typing import List
from copy import copy, deepcopy
from math import inf, isinf
from heapq import heappush, heappop
from typing import Any, Mapping, Tuple, List


def dijkstra(graph, start, goal) -> Tuple[float, List]:
    """
    Find the shortest distance between two nodes in a graph, and
    the path that produces that distance.

    The graph is defined as a mapping from Nodes to a Map of nodes which
    can be directly reached from that node, and the corresponding distance.

    Returns:
        A tuple containing
            - the distance between the start and goal nodes
            - the path as a list of nodes from the start to goal.

    If no path can be found, the distance is returned as infinite, and the
    path is an empty list.
    """

    shortest_distance = {}
    predecessor = {}
    heap = []

    heappush(heap, (0, start, None))

    while heap:

        distance, node, previous = heappop(heap)

        if node in shortest_distance:
            continue

        shortest_distance[node] = distance
        predecessor[node] = previous

        if node == goal:

            path = []
            while node:
                path.append(node)
                node = predecessor[node]

            return distance, path[::-1]

        else:
            for successor, dist in graph[node].items():
                heappush(heap, (distance + dist, successor, node))

    else:

        return inf, []


class mylist(list):
    def __getitem__(self, n):
        if n < 0:
            raise IndexError("...")
        return list.__getitem__(self, n)


def get_connections(nodes: List[int], row: int, col: int):
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


def cycle(num: int) -> int:
    if num == 9:
        return 1
    return num + 1


def extend_row(row):
    rows = [row]
    while len(rows) < 5:
        rows.append(mylist(map(cycle, rows[-1])))
    return mylist(item for sublist in rows for item in sublist)


def extend_vertically(nodes_input):
    sections = [nodes_input]
    while len(sections) < 5:
        last_section = deepcopy(sections[-1])
        for row in range(len(last_section)):
            last_section[row] = mylist(map(cycle, last_section[row]))
        sections.append(last_section)
    return mylist(item for sublist in sections for item in sublist)


filename = "day15.txt"
debug = "AoC-John/Day15/" + filename

with open(debug) as file:
    file_content = file.readlines()
    file_content = mylist(line.strip() for line in file_content)
    nodes_input = mylist()
    for line in file_content:
        nodes_input.append(mylist(int(num) for num in list(line)))

    for row in range(len(nodes_input)):
        nodes_input[row] = extend_row(nodes_input[row])

    nodes_input = extend_vertically(nodes_input)

    # for row in nodes_input:
    #     print("".join(map(str, row)))

    nodes = defaultdict(dict)
    for row in range(len(nodes_input)):
        for col in range(len(nodes_input[0])):
            nodes[(row, col)] = get_connections(nodes_input, row, col)

    for node in nodes:
        if (0, 0) in nodes[node]:
            del nodes[node][(0, 0)]

    distance, path = dijkstra(
        nodes, (0, 0), (len(nodes_input) - 1, len(nodes_input) - 1)
    )

    print(f"Final distance: {distance}")
