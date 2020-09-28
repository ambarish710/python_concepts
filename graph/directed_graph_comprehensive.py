from queue import Queue


# Graph
class Graph:
    def __init__(self, edges_list):
        self.adjacency_list = {}
        self.bfs_parent = {}
        self.dfs_parent = {}
        self.visited = {}
        self.color = {}
        self.bfs_traversal_output = []
        self.dfs_traversal_output = []
        self.bfs_queue = Queue()
        for start_vertice, end_vertice in edges_list:
            # Check 1
            if start_vertice not in self.adjacency_list:
                self.adjacency_list[start_vertice] = [end_vertice]
            else:
                self.adjacency_list[start_vertice].append(end_vertice)

            # Check 2
            if end_vertice not in self.adjacency_list:
                self.adjacency_list[end_vertice] = []

        for node in self.adjacency_list:
            self.bfs_parent[node] = None
            self.dfs_parent[node] = None
            self.visited[node] = False
            # If node not visited then color white
            # If node visited then color grey
            # If nodes all children visited then black
            self.color[node] = "White"

        print(self.adjacency_list)
        print(self.bfs_parent)
        print(self.dfs_parent)
        print(self.visited)
        print(self.color)   




    # Breadth First Search of Directed Graph
    def bfs_traversal(self, node):
        self.visited[node] = True
        self.bfs_queue.put(node)
        while not self.bfs_queue.empty():
            vertice = self.bfs_queue.get()
            self.bfs_traversal_output.append(vertice)
            for connected_node in self.adjacency_list[vertice]:
                if not self.visited[connected_node]:
                    self.bfs_queue.put(connected_node)
                    self.bfs_parent[connected_node] = vertice
                    self.visited[connected_node] = True


    # Depth First Search of Directed Graph
    def dfs_traversal(self, node):
        self.color[node] = "Grey"
        self.dfs_traversal_output.append(node)
        for vertice in self.adjacency_list[node]:
            if self.color[vertice] == "White":
                self.dfs_traversal(vertice)
                self.dfs_parent[vertice] = node
        self.color[node] = "Black"


    # Find Cycle in Directed Graph
    def find_cycle(self, node):
        pass


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

    graph_obj = Graph(edges_list=edges_list)

    print("BFS Graph Traversal Output --\n")
    graph_obj.bfs_traversal(node="A")
    print(graph_obj.bfs_traversal_output)
    print(graph_obj.bfs_parent)

    print("DFS Graph Traversal Output --\n")
    graph_obj.dfs_traversal(node="A")
    print(graph_obj.dfs_traversal_output)
    print(graph_obj.dfs_parent)

    # print("Cycle/Loop found in Graph Traversal Output -- {}".format(graph_obj.find_cycle(node="A")))
