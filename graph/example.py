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

    def bfs_traversal(self, start):
        self.node_color[start] = "Grey"
        self.traversed_list.append(start)
        if start in self.graph_dict:
            for vertice in self.graph_dict[start]:
                if vertice not in self.traversed_list:
                    self.dfs_traversal(start=vertice)
        self.node_color[start] = "Black"


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
