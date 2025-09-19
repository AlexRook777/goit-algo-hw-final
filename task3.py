import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        """
        Add an edge to the graph.

        :param u: The first vertex of the edge.
        :param v: The second vertex of the edge.
        :param weight: The weight of the edge.
        """
        if u not in self.edges:
            self.edges[u] = []
        self.edges[u].append((v, weight)) # додавання ребра від u до v з вагою weight
        if v not in self.edges:
            self.edges[v] = []
        self.edges[v].append((u, weight)) # додавання ребра від v до u з вагою weight (для неорієнтованого графа)

    def deykstrea(self, start):
        """
        Визначає найкоротші відстані від початку до всіх інших вершин графа.

        :param start: Вершина, з якої починається пошук.
        :return: Словник, де ключ - вершина, а значення - найкоротша відстань від початку до цієї вершини.
        """
        distances = {vertex: float('inf') for vertex in self.edges} # Ініціалізація відстаней до всіх вершин як нескінченність
        distances[start] = 0 # Відстань до початкової вершини дорівнює 0
        heap = [(0, start)] # Мін-heap для пріоритетного вибору вершини з найменшою відстанню
        visited = set() # Множина відвіданих вершин

        while heap:
            current_distance, current_vertex = heapq.heappop(heap) # Вибір вершини з найменшою відстанню
            if current_vertex in visited:
                continue
            visited.add(current_vertex)

            for neighbor, weight in self.edges.get(current_vertex, []): # Перебір сусідів поточної вершини
                distance = current_distance + weight # Обчислення відстані до сусіда через поточну вершину
                if distance < distances.get(neighbor, float('inf')): # Якщо знайдена відстань менша за відому
                    distances[neighbor] = distance # Оновлення найкоротшої відстані до сусіда
                    heapq.heappush(heap, (distance, neighbor)) # Додавання сусіда до heap для подальшої обробки
        return distances

if __name__ == "__main__":
    # Приклад використання
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 6)
    g.add_edge('C', 'D', 1)
    g.add_edge('D', 'E', 3)

    start_vertex = 'A'
    shortest_paths = g.deykstrea(start_vertex)
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"{vertex}: {distance}")