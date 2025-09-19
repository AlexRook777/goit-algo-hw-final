import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#cccccc"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, highlight_nodes=None, title=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = []
    for node in tree.nodes(data=True):
        node_id = node[0]
        if highlight_nodes and node_id in highlight_nodes:
            colors.append(highlight_nodes[node_id])
        else:
            colors.append(node[1]['color'])
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    if title:
        plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_to_tree(heap):
    if not heap:
        return None
    nodes = [Node(val) for val in heap]
    n = len(heap)
    for i in range(n):
        left_i = 2 * i + 1
        right_i = 2 * i + 2
        if left_i < n:
            nodes[i].left = nodes[left_i]
        if right_i < n:
            nodes[i].right = nodes[right_i]
    return nodes[0]

def get_gradient_color(index, total, base="#1296F0"):
    # Від темного до світлого відтінку base
    """
    Generates a gradient color from base to white, given the index and total number of nodes.
    
    :param int index: The index of the node in the order of visualization.
    :param int total: The total number of nodes in the visualization.
    :param str base: The base color of the gradient in hexadecimal format. Default is "#1296F0".
    :return: A string representing the gradient color in hexadecimal format.
    """
    base = base.lstrip("#")
    r, g, b = int(base[0:2], 16), int(base[2:4], 16), int(base[4:6], 16)
    factor = 0.2 + 0.6 * (index / max(1, total-1))  # 0.4..1.0
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    return f"#{r:02x}{g:02x}{b:02x}"

def bfs_visualize(root):
    """
    Visualizes the given tree using BFS traversal.

    :param root: The root of the tree to be visualized.
    :return: A list of nodes in the order of their BFS traversal.
    """

    queue = deque([root])
    order = []
    visited = set()
    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)
            queue.append(node.left)
            queue.append(node.right)
    # Присвоюємо кольори
    highlight = {}
    for idx, node in enumerate(order):
        highlight[node.id] = get_gradient_color(idx, len(order), "#1296F0")
    draw_tree(root, highlight, title="BFS Traversal")
    return order

def dfs_visualize(root):
    """
    Visualizes the given tree using DFS traversal.

    :param root: The root of the tree to be visualized.
    :return: A list of nodes in the order of their DFS traversal.
    """
    stack = [root]
    order = []
    visited = set()
    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            order.append(node)
            visited.add(node.id)
            # Спочатку правий, потім лівий (щоб лівий був першим)
            stack.append(node.right)
            stack.append(node.left)
    # Присвоюємо кольори
    highlight = {}
    for idx, node in enumerate(order):
        highlight[node.id] = get_gradient_color(idx, len(order), "#F07F12")
    draw_tree(root, highlight, title="DFS Traversal")
    return order

if __name__ == "__main__":
    heap = [10, 7, 9, 2, 6, 8]
    root = heap_to_tree(heap)
    print("BFS (в ширину):")
    bfs_visualize(root)
    print("DFS (у глибину):")
    dfs_visualize(root)