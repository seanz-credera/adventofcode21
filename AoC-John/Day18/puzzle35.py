from collections import defaultdict
from typing import DefaultDict
import pprint


class Node:
    def __init__(self, key: str) -> None:
        self.key = key
        self.left = None
        self.right = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "%s" % self.key
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.key
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.key
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# Convert snailfish list to tree where each node is list,
# each child is content of that list
def to_tree(snailfish):
    root = Node(str(snailfish))
    if type(snailfish) is list:
        root.left = to_tree(snailfish[0])
        root.right = to_tree(snailfish[1])
    return root


# Function to find the depth of
# a given node in a Binary Tree
def findDepth(root, x):

    # Base case
    if root == None:
        return -1

    # Initialize distance as -1
    dist = -1

    # Check if x is current node=
    if root.key == x:
        return dist + 1

    dist = findDepth(root.left, x)
    if dist >= 0:
        return dist + 1
    dist = findDepth(root.right, x)
    if dist >= 0:
        return dist + 1
    return dist


# Helper function to find the height
# of a given node in the binary tree
def findHeightUtil(root, x):
    global height
    # Base Case
    if root == None:
        return -1

    # Store the maximum height of
    # the left and right subtree
    leftHeight = findHeightUtil(root.left, x)

    rightHeight = findHeightUtil(root.right, x)

    # Update height of the current node
    ans = max(leftHeight, rightHeight) + 1

    # If current node is the required node
    if root.key == x:
        height = ans

    return ans


# Function to find the height of
# a given node in a Binary Tree
def findHeight(root, x):
    global height

    # Stores height of the Tree
    maxHeight = findHeightUtil(root, x)

    # Return the height
    return height


filename = "day18.txt"
debug = "AoC-John/Day18/" + filename

test = eval("[7,[6,[5,[4,[3,2]]]]]")
test = to_tree(test)
test2 = eval("[[[[[9,8],1],2],3],4]")
test2 = to_tree(test2)
test3 = eval("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
test3 = to_tree(test3)

test.display()
print(f"\nHeight: {findHeight(test, test.key)}")

test2.display()
print(f"\nHeight: {findHeight(test2, test2.key)}")

test3.display()
print(f"\nHeight: {findHeight(test3, test3.key)}")

print(f"Depth of [7, 3]: {findDepth(test3, '[7, 3]')}")
print(f"Depth of [3, 2]: {findDepth(test3, '[3, 2]')}")

# with open(debug) as file:
#     file_content = file.readlines()
#     file_content = [eval(line.strip()) for line in file_content]
#     snailfish_num = file_content[0]
#     for i in range(1, len(file_content) - 1):
#         snailfish_num = [snailfish_num] + [file_content[i]]
#         while not is_reduced(snailfish_num):
#             snailfish_num = reduce(snailfish_num)
