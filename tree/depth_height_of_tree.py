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


    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            # if (lDepth > rDepth):
            #     return lDepth + 1
            # else:
            #     return rDepth + 1
            return max(lDepth, rDepth) + 1


def tree_adder(data_list):
    root = BinarySearchTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])
    return root


if __name__ == "__main__":
    data_list = [25, 3, 4, 56, 77, 29, 1, 5, 3, 2, 1]
    root = tree_adder(data_list)
    print(root.maxDepth(node=root))
