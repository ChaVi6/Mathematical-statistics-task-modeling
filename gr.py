

p1 = 0.4
p2 = 0.3
p3 = 0.5
q1 = 1 - p1
q2 = 1 - p2
q3 = 1 - p3

# b1 -> b2   (p1)
# b2 -> b3   (p2)
# b3 -> b4   (p3)
# b1 -> b3   (q1)
# b2 -> b4   (q2)
# b3 -> b2   (q3)

class Graph:
    def __init__(self, edges, n):
        self.adjList = [None] * n
        for i in range(n):
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))

def printGraph(graph):
    for src in range(len(graph.adjList)):
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()


if __name__ == '__main__':

    # Вход #: ребра во взвешенном орграфе (согласно приведенной выше диаграмме)
    # Ребро (x, y, w) представляет собой ребро от `x` до `y`, имеющее вес `w`
    edges = [(1, 2, p1), (1, 3, q1), (2, 3, p2), (2, 4, q2),
             (3, 2, q3), (3, 4, p3)]

    # Количество вершин (от 0 до 5)
    n = 4

    # построить graph из заданного списка ребер
    graph = Graph(edges, n)

    # печатать представление списка смежности Graph
    printGraph(graph)
