def inorder_traversal(self):
    sorted_list = []
    if self.left:
        sorted_list += self.left.inorder_traversal()
    sorted_list.append(self.data)
    if self.right:
        sorted_list += self.right.inorder_traversal()
    return sorted_list