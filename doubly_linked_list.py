"""
    Few tip while iterating over arrays recursively --
    1. Always make sure you check (if ptr == None) should always be before the next iteration jump
    2. Always make next iteration jump directly while calling the function,
            CORRECT APPROACH
                if ptr == None:
                    return
                ret_str = self.print_dll_rev(ptr.next)          --> DO THIS INSTEAD
                print(ptr.data)

            WRONG APPROACH
                if ptr ==  None:
                    return
                ptr = ptr.next                                  --> DON'T DO THIS
                ret_str = self.print_dll_rev(ptr)
                print(ptr.data)
"""


class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_element_at_start(self, data):
        if self.head == None:
            node_obj = Node(data=data)
            self.head = node_obj
        else:
            node_obj = Node(data=data, next=self.head)
            self.head.prev = node_obj
            self.head = node_obj


    def add_element_at_end(self, data):
        if self.head == None:
            node_obj = Node(data=data)
            self.head = node_obj
        iteration_obj = self.head
        while iteration_obj != None:
            prev_obj = iteration_obj
            iteration_obj = iteration_obj.next
        node_obj = Node(data=data, prev=prev_obj)
        prev_obj.next = node_obj


    def print_dll_fwd(self):
        iteration_obj = self.head
        dll_str = ""
        while iteration_obj:
            if iteration_obj.next == None:
                dll_str += str(iteration_obj.data)
            else:
                dll_str += str(iteration_obj.data) + "-->"
            iteration_obj = iteration_obj.next
        print(dll_str)


    def print_dll_rev(self, ptr):
        if ptr == None:
            return
        ret_str = self.print_dll_rev(ptr.next)
        if ret_str:
            if ptr.prev == None:
                ret_str += str(ptr.data)
            else:
                ret_str += str(ptr.data) + "-->"
        else:
            ret_str = str(ptr.data) + "-->"
        return(ret_str)


    def dll_length(self):
        iteration_obj =  self.head
        iteration_count = 0
        while iteration_obj:
            iteration_count += 1
            iteration_obj = iteration_obj.next
        print(iteration_count)
        return iteration_count


    def delete_element_at(self, location):
        dll_len = self.dll_length()
        if location > dll_len or location < 0:
            print("Location number out of linked list range")
            print("Please provide a number in between 0-{}".format(dll_len))
        elif location == 1:
            self.head = self.head.next
            self.head.prev = None
        else:
            iteration_obj = self.head
            for i in range(0, location-1):
                iteration_obj = iteration_obj.next
            prev = iteration_obj.next.prev
            iteration_obj.next = iteration_obj.next.next
            iteration_obj.next.prev = prev


    def delete_element_at_start(self):
        if self.head ==  None:
            print("Linked List empty!")
            return
        elif self.dll_length() == 1:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev =  None


    def delete_element_at_end(self):
        dll_len = self.dll_length()
        if self.head == None:
            print("Linked List empty!")
            return
        elif dll_len == 1:
            self.head = None
        else:
            iteration_obj =  self.head
            for i in range(0, dll_len-2):
                iteration_obj =  iteration_obj.next
            iteration_obj.next = None


if __name__ == "__main__":
    dll_obj = DoublyLinkedList()
    dll_obj.add_element_at_start(15)
    dll_obj.add_element_at_start(10)
    dll_obj.add_element_at_end(20)
    dll_obj.add_element_at_start(5)
    dll_obj.add_element_at_end(25)
    dll_obj.print_dll_fwd()
    dll_obj.dll_length()
    print(dll_obj.print_dll_rev(dll_obj.head))
    dll_obj.delete_element_at(2)
    dll_obj.dll_length()
    dll_obj.print_dll_fwd()
    print(dll_obj.print_dll_rev(dll_obj.head))
    dll_obj.delete_element_at_start()
    dll_obj.dll_length()
    dll_obj.print_dll_fwd()
    print(dll_obj.print_dll_rev(dll_obj.head))
    dll_obj.delete_element_at_end()
    dll_obj.dll_length()
    dll_obj.print_dll_fwd()
    print(dll_obj.print_dll_rev(dll_obj.head))

