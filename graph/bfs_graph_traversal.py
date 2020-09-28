from queue import Queue


# Undirected Graph
class Graph:
    def __init__(self, edges_list):
        self.graph_adjacency_list = {}
        self.parent = {}
        self.level = {}
        self.visited = {}
        self.bfs_queue = Queue()
        self.bfs_traversal_output = []
        for start, end in edges_list:
            # Directon 1
            if start not in self.graph_adjacency_list:
                self.graph_adjacency_list[start] = [end]
            else:
                self.graph_adjacency_list[start].append(end)

            # Directon 2
            if end not in self.graph_adjacency_list:
                self.graph_adjacency_list[end] = [start]
            else:
                self.graph_adjacency_list[end].append(start)

        for vertice in self.graph_adjacency_list:
            self.visited[vertice] = False
            self.parent[vertice] = None
            self.level[vertice] = -1

        print(self.graph_adjacency_list)


    def bfs_traversal(self, start):
        self.level[start] = 0
        self.visited[start] = True
        self.bfs_queue.put(start)
        while not self.bfs_queue.empty():
            vertice = self.bfs_queue.get()
            self.bfs_traversal_output.append(vertice)
            for connected_node in self.graph_adjacency_list[vertice]:
                if not self.visited[connected_node]:
                    self.bfs_queue.put(connected_node)
                    self.parent[connected_node] = vertice
                    self.level[connected_node] = self.level[vertice] + 1
                    self.visited[connected_node] = True
        print(self.bfs_traversal_output)


    def shortest_path(self, node):
        self.shortest_path = [node]
        if node:
            while self.parent[node] != None:
                self.shortest_path.append(self.parent[node])
                node = self.parent[node]
        self.shortest_path.reverse()
        return self.shortest_path


if __name__ == "__main__":
    edges_list = [
        ("A", "B"),
        ("A", "D"),
        ("B", "C"),
        ("D", "E"),
        ("D", "F"),
        ("E", "F"),
        ("E", "G"),
        ("F", "H"),
        ("G", "H")
    ]

    g_obj = Graph(edges_list=edges_list)
    g_obj.bfs_traversal(start="A")
    print(g_obj.parent)
    shortest_path = g_obj.shortest_path(node="H")
    print("Shortest Path: {}".format(shortest_path))
