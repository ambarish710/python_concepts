#https://github.com/codebasics/py/blob/master/DataStructures/7_Tree/7_tree_exercise.md
class GeneralTreeNode:
    def __init__(self, data):
        self.parent = None
        self.data = data
        self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def node_level(self):
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level

    def print_tree_by_level(self, input_level):
        level = self.node_level()
        if level <= input_level:
            spacing = (" " * level * 4 + "|__ ") if level > 0 else ""
            print(str(spacing) + str(self.data))
            for child in self.children:
                child.print_tree_by_level(input_level)


if __name__ == "__main__":
    root = GeneralTreeNode("Global")

    india = GeneralTreeNode("India")
    gujrat = GeneralTreeNode("Gujrat")
    ahemdabad = GeneralTreeNode("Ahemdabad")
    baroda = GeneralTreeNode("Baroda")
    kartanka = GeneralTreeNode("Karnataka")
    banglore = GeneralTreeNode("Bangluru")
    mysore = GeneralTreeNode("Mysore")

    usa = GeneralTreeNode("USA")
    nj = GeneralTreeNode("New Jersey")
    princeton = GeneralTreeNode("Princeton")
    trenton = GeneralTreeNode("Trenton")

    cali = GeneralTreeNode("California")
    sf = GeneralTreeNode("San Francisco")
    mv = GeneralTreeNode("Mountain View")
    paloalto = GeneralTreeNode("Palo Alto")

    root.add_child(india)
    root.add_child(usa)

    india.add_child(gujrat)
    india.add_child(kartanka)

    gujrat.add_child(ahemdabad)
    gujrat.add_child(baroda)

    kartanka.add_child(banglore)
    kartanka.add_child(mysore)

    usa.add_child(cali)
    usa.add_child(nj)

    nj.add_child(princeton)
    nj.add_child(trenton)

    cali.add_child(sf)
    cali.add_child(mv)
    cali.add_child(paloalto)

    # Print tree on level given
    print("\nPrinting tree by given input level--")
    root.print_tree_by_level(input_level=1)

    print("\nPrinting tree by given input level--")
    root.print_tree_by_level(input_level=2)

    print("\nPrinting tree by given input level--")
    root.print_tree_by_level(input_level=3)
