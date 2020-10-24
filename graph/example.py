# White Node not traversed
# Grey means Node is traversed
# Black means Node's child also traversed

class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        self.node_color = {}
        self.traversed_list = []
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                self.node_color[start] = "White"
        print("Graph Dictionary: {}".format(self.graph_dict))

    def dfs_traversal(self, start):
        self.node_color[start] = "Grey"
        self.traversed_list.append(start)
        if start in self.graph_dict:
            for vertice in self.graph_dict[start]:
                if vertice not in self.traversed_list:
                    self.dfs_traversal(start=vertice)
        self.node_color[start] = "Black"

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


if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]
    g_obj = Graph(routes)
    print("\nNode Color: {}".format(g_obj.node_color))
    g_obj.dfs_traversal(start="Mumbai")
    print("\nTraversed List: {}".format(g_obj.traversed_list))
    print("\nNode Color: {}".format(g_obj.node_color))
