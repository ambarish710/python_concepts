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

    def preorder_traversal(self):
        sorted_list = []
        sorted_list.append(self.data)
        if self.left:
            sorted_list += self.left.preorder_traversal()
        if self.right:
            sorted_list += self.right.preorder_traversal()
        return sorted_list

    def postorder_traversal(self):
        sorted_list = []
        if self.left:
            sorted_list += self.left.postorder_traversal()
        if self.right:
            sorted_list += self.right.postorder_traversal()
        sorted_list.append(self.data)
        return sorted_list

    def bst_search(self, input_value):
        if self.data == input_value:
            return True

        if input_value < self.data:
            if self.left:
                return self.left.bst_search(input_value)
            else:
                return False

        else:
            if self.right:
                return self.right.bst_search(input_value)
            else:
                return False

    def bst_min(self):
        if self.left:
            return self.left.bst_min()
        else:
            return self.data

    def bst_max(self):
        if self.right:
            return self.right.bst_max()
        else:
            return self.data

    def bst_total(self):
        sorted_list = 0
        if self.left:
            sorted_list += self.left.bst_total()
        sorted_list += self.data
        if self.right:
            sorted_list += self.right.bst_total()
        return sorted_list

def tree_adder(data_list):
    root = BinarySearchTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])
    return root

if __name__ == "__main__":
    data_list = [25,3,4,56,77,29,1,5,3,2,1]
    root = tree_adder(data_list)
    print(root.postorder_traversal())
    print(root.preorder_traversal())
    print(root.inorder_traversal())
    print(root.bst_max())
    print(root.bst_min())
    print(root.bst_total())
    print(root.bst_search(25))
