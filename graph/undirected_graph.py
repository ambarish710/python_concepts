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

        if end not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end):
        # Approach 1
        paths_list = self.get_paths(start, end)
        if paths_list:
            if len(paths_list) > 1:
                shortest_path = [paths_list[0]]
                for i in range(1, len(paths_list)):
                    if len(paths_list[i]) > len(shortest_path[0]):
                        pass
                    elif len(paths_list[i]) == len(shortest_path[0]):
                        shortest_path.append(paths_list[i])
                    else:
                        shortest_path = [paths_list[i]]
                return shortest_path
            else:
                return paths_list
        else:
            return []

        # Approach 2
        # path = path + [start]
        #
        # if start == end:
        #     return [path]
        #
        # if end not in self.graph_dict:
        #     return []
        #
        # paths = []
        # for node in self.graph_dict[start]:
        #     if node not in path:
        #         new_paths = self.get_paths(node, end, path)
        #         for p in new_paths:
        #             paths.append(p)
        # return paths

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
    print(paths)

    shortest_path = g_obj.get_shortest_path(start="Mumbai", end="New York")
    print(shortest_path)
