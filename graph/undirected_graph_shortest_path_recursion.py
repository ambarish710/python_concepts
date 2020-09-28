class Graph:
    def __init__(self, edges):
        self.graph_dict = {}
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dictionary: {}".format(self.graph_dict))

    def get_paths(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            new_paths = self.get_paths(start=node, end=end, path=path)
            for p in new_paths:
                paths.append(p)

        return paths


    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            new_paths = self.get_paths(start=node, end=end, path=path)
            for p in new_paths:
                if paths:
                    if len(paths[0]) > len(p):
                        paths = [p]
                    elif len(paths[0]) == len(p):
                        paths.append(p)
                    else:
                        pass
                else:
                    paths.append(p)

        return paths

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
    paths = g_obj.get_paths(start="Mumbai", end="New York")
    print("All Paths between {} and {}: {}".format("Mumbai", "New York", paths))
    shortest_path = g_obj.get_shortest_path(start="Mumbai", end="New York")
    print("Shortest Path {} and {}: {}".format("Mumbai", "New York", shortest_path))
