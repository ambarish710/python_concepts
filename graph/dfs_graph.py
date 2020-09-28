class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        self.traversed_node = []
        self.node_color = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
                self.node_color[start] = "White"
        print("Graph Dict: {}".format(self.graph_dict))

    def depth_first_search(self, start):
        self.node_color[start] = "Grey"
        self.traversed_node.append(start)
        if start in self.graph_dict:
            for vertice in self.graph_dict[start]:
                if vertice not in self.traversed_node:
                    self.depth_first_search(start=vertice)
        self.node_color[start] = "Black"

if __name__ == "__main__":
    routes2 = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    g_obj = Graph(routes2)
    print("\nNode Color Dict: {}".format(g_obj.node_color))
    g_obj.depth_first_search(start="Mumbai")
    print("\nNode Traversed List: {}".format(g_obj.traversed_node))
    print("\nNode Color Dict: {}".format(g_obj.node_color))
