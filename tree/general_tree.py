# General Tree basic use case
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

    def print_tree(self):
        level = self.node_level()
        spacing = (" " * level * 4 + "|__ ") if level > 0 else ""
        print(str(spacing) + str(self.data))
        for child in self.children:
            child.print_tree()

    def print_tree_by_level(self, input_level):
        level = self.node_level()
        if level <= input_level:
            spacing = (" " * level * 4 + "|__ ") if level > 0 else ""
            print(str(spacing) + str(self.data))
            for child in self.children:
                child.print_tree_by_level(input_level)


if __name__ == "__main__":
    root = GeneralTreeNode("Electronics")

    laptop = GeneralTreeNode("Laptop")
    macbook = GeneralTreeNode("Macbook")
    microsoftsurface = GeneralTreeNode("Microsoft Surface")
    thinkpad = GeneralTreeNode("Thinkpad")
    laptop.add_child(macbook)
    laptop.add_child(microsoftsurface)
    laptop.add_child(thinkpad)

    cellphones = GeneralTreeNode("Cell Phones")
    iphone = GeneralTreeNode("Iphone")
    googlepixel = GeneralTreeNode("Google Pixel")
    vivo = GeneralTreeNode("Vivo")
    cellphones.add_child(iphone)
    cellphones.add_child(googlepixel)
    cellphones.add_child(vivo)

    televisions = GeneralTreeNode("Televisions")
    samsung = GeneralTreeNode("Samsung")
    lg = GeneralTreeNode("LG")
    televisions.add_child(samsung)
    televisions.add_child(lg)

    root.add_child(laptop)
    root.add_child(cellphones)
    root.add_child(televisions)
    root.print_tree()

    # Print tree on level given
    print("\nPrinting tree by given input level--")
    root.print_tree_by_level(input_level=1)
