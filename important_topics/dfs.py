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

    def inorder_traversal(self):
        sorted_list = []
        if self.left:
            sorted_list += self.left.inorder_traversal()
        sorted_list.append(self.data)
        if self.right:
            sorted_list += self.right.inorder_traversal()
        return sorted_list


def tree_adder(data_list):
    root = BinarySearchTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])
    return root


if __name__ == "__main__":
    data_list = [25,3,4,56,77,29,1,5,3,2,1]
    root = tree_adder(data_list)
    print(root.inorder_traversal())
