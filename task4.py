import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    """
    Ініціалізація вузла з заданим ключем та кольором.

    :param key: Ключ вузла.
    :param color: Кольор вузла (за замовчанням "skyblue").
    """
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """
    Рекурсивно додає до графа вузлів з дерева та їх координати.

    :param graph: Граф, до якого додається вузли.
    :param node: Корінь дерева, з якого починається рекурсивне додавання.
    :param pos: Словник, де ключ - ідентифікатор вузла, а значення - координати вузла.
    :param x: Початкова координата x вузла.
    :param y: Початкова координата y вузла.
    :param layer: Рівень рекурсії, що залишився.
    :return: Оновлений граф з вузлами дерева.
    """
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    """
    Малює дерево з вузлами, що представляє граф (NetworkX).

    :param tree_root: Корінь дерева, з якого починається малювання.
    :return: None
    """

    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def heap_to_tree(heap):
    """
    Перетворює масив бінарної купи у дерево Node.
    :param heap: Список чисел, що представляє бінарну купу.
    :return: Корінь дерева Node.
    """
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


if __name__ == "__main__":

    # Візуалізація бінарної купи
    heap = [10, 7, 9, 2, 6, 8]
    heap_root = heap_to_tree(heap)
    draw_tree(heap_root)


