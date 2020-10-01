from queue import Queue


class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None


    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)


    def bfs_level_order_traversal(self):
        bfs_output = []
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            self = queue.get()
            #print(self.data)
            bfs_output.append(self.data)

            if self.left:
                queue.put(self.left)

            if self.right:
                queue.put(self.right)
        return bfs_output


    def dfs_inorder_traversal(self):
        dfs_output = []
        if self.left:
            dfs_output += self.left.dfs_inorder_traversal()
        dfs_output.append(self.data)
        if self.right:
            dfs_output += self.right.dfs_inorder_traversal()
        return dfs_output


def tree_adder(data_list):
    root = BinarySearchTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])
    return root


if __name__ == "__main__":
    data_list = [25, 3, 4, 56, 77, 29, 1, 5, 3, 2, 1]
    root = tree_adder(data_list)

    levelorder_data = root.bfs_level_order_traversal()
    print("Level order data: {}".format(levelorder_data))

    inorder_data = root.dfs_inorder_traversal()
    print("In order data: {}".format(inorder_data))


