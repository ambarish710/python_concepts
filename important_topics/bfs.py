
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

    def bfs_level_order_traversal_with_sentinel(self):
        queue = Queue()
        sentinel = "#"
        queue.put(sentinel)
        queue.put(self)

        while queue.qsize() > 1:
            node = queue.get()
            if node == "#":
                print("\n")
                queue.put(sentinel)
            else:
                print(node.data)

                if node.left:
                    queue.put(node.left)

                if node.right:
                    queue.put(node.right)

    def bfs_level_order_traversal_with_sentinel_with_list(self):
        ret = []
        cut = 0
        queue = Queue()
        sentinel = "#"
        queue.put(sentinel)
        queue.put(self)

        while queue.qsize() > 1:
            node = queue.get()
            if node == "#":
                ret += [[]]
                queue.put(sentinel)
                cut += 1
            else:
                if cut % 2 == 0:
                    ret[-1].insert(0, node.data)
                else:
                    ret[-1].append(node.data)

                if node.left:
                    queue.put(node.left)

                if node.right:
                    queue.put(node.right)

        return ret


    def dfs_inorder_traversal(self):
        dfs_output = []
        if self.left:
            dfs_output += self.left.dfs_inorder_traversal()
        dfs_output.append(self.data)
        if self.right:
            dfs_output += self.right.dfs_inorder_traversal()
        return dfs_output


    def closestValue(self, target):
        if self == None:
            return None

        closest = self.data
        difference = abs(target - closest)
        queue = Queue()
        queue.put(self)

        print("YYY -- {}".format(closest))
        print("\n")

        while not queue.empty():
            print("XXX")
            self = queue.get()
            if self.data != None:
                print("Value {} -- Current Diff {} -- Diff {} -- Curent Vale {}".format(self.data, difference, abs(self.data - target), closest))
                if abs(self.data - target) < difference:
                    print("Changing now")
                    closest = self.data
                    difference = self.data - target

            if self.left:
                queue.put(self.left)

            if self.right:
                queue.put(self.right)

            print("WWW -- {}".format(closest))
            print("\n")

        print("ZZZ -- {}".format(closest))
        return closest


def tree_adder(data_list):
    root = BinarySearchTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])
    return root


if __name__ == "__main__":
    data_list = [25, 3, 4, 56, 77, 29, 1, 5, 3, 2, 1]
    #data_list = [3,1,4,None,2]
    #data_list = [4,2,5,1,3]
    root = tree_adder(data_list)

    # levelorder_data = root.bfs_level_order_traversal()
    # print("Level order data: {}".format(levelorder_data))

    print(root.bfs_level_order_traversal_with_sentinel())

    # inorder_data = root.dfs_inorder_traversal()
    # print("In order data: {}".format(inorder_data))
    #
    # output = root.closestValue(target=0.428571)
    # print(output)
