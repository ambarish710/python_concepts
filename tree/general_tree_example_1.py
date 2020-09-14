#https://github.com/codebasics/py/blob/master/DataStructures/7_Tree/7_tree_exercise.md
# Print data1 from tree, print data2 from tree, print both
# General tree hierarchy

class GeneralTreeNode:
    def __init__(self, name, designation):
        self.parent = None
        self.data = [name, designation]
        self.children = []

    def add_child(self, child):
        child.parent  = self
        self.children.append(child)

    def get_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_required(self, delimiter):
        level = self.get_level()
        prefix = " " * level * 4 + "|__" if level > 0 else ""
        if delimiter == "both":
            print(str(prefix) + str(self.data[0]) + " ({})".format(self.data[1]))
        elif delimiter == "name":
            print(str(prefix) + self.data[0])
        elif delimiter == "designation":
            print(str(prefix) + self.data[1])
        for child in self.children:
            child.print_required(delimiter)


if __name__ == "__main__":
    root = GeneralTreeNode(name="Nilupul", designation="CEO")

    chinmay = GeneralTreeNode(name="Chinmay", designation="CTO")
    gels = GeneralTreeNode(name="Gels", designation="HR Head")
    root.add_child(chinmay)
    root.add_child(gels)

    vishwa = GeneralTreeNode(name="Vishwa", designation="Infrastructure Head")
    aamir = GeneralTreeNode(name="Aamir", designation="Application Head")
    chinmay.add_child(vishwa)
    chinmay.add_child(aamir)

    dhaval = GeneralTreeNode(name="Dhaval", designation="Cloud Manager")
    abhijit = GeneralTreeNode(name="Abhijit", designation="App Manager")
    vishwa.add_child(dhaval)
    vishwa.add_child(abhijit)

    peter = GeneralTreeNode(name="Peter", designation="Recruitment Manager")
    waqar = GeneralTreeNode(name="Waqar", designation="Policy Manager")
    gels.add_child(peter)
    gels.add_child(waqar)

    root.print_required(delimiter="both")
    print("\n")

    root.print_required(delimiter="name")
    print("\n")

    root.print_required(delimiter="designation")
    print("\n")
