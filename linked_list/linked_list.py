class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_element_at_beginning_in_linked_list(self, data):
        node_obj = Node(data, self.head)
        self.head = node_obj


    def print_all_elements_in_linked_list(self):
        if self.head == None:
            print("List is empty")
            return

        iterator = self.head
        output_str = ""
        while iterator:
            if iterator.next == None:
                output_str += str(iterator.data)
            else:
                output_str += str(iterator.data) + "-->"
            iterator = iterator.next
        print(output_str)


    def length_of_linked_list(self):
        iterator = self.head
        linked_list_len = 0
        while iterator:
            linked_list_len += 1
            iterator = iterator.next
        print("Linked List length is: {}".format(linked_list_len))
        return linked_list_len


    def insert_element_at_the_end_of_linked_list(self, data):
        iterator = self.head
        if self.head == None:
            node_obj = Node(data)
            self.head = node_obj
            return
        # while iterator:
        #     iterator = iterator.next
        #     if iterator.next == None:
        #         iterator.next = Node(data)
        #         return
        while iterator.next:
            iterator = iterator.next
        iterator.next = Node(data)
        return


    def create_linked_list_for_bulk_input(self, bulk_input):
        for data in bulk_input:
            self.insert_element_at_the_end_of_linked_list(data)


    def deleting_an_element_from_linked_list_at_given_index(self, location):
        linked_list_len = self.length_of_linked_list()
        print("Length of LL - {}, delete element at location - {}".format(linked_list_len, location))
        if location > linked_list_len or location < 0:
            print("Index value out of range, please provide value in between 0-{}".format(linked_list_len))
        elif location == 1:
            self.head = self.head.next
        else:
            iteration_object = self.head
            for i in range(0, location-1):
                iteration_object = iteration_object.next
            iteration_object.next = iteration_object.next.next


    def inserting_element_at_given_location_in_a_linked_list(self, location, data):
        linked_list_len = self.length_of_linked_list()
        if linked_list_len < location:
            print("Please provide insertion location in range 0-{}".format(linked_list_len))
        elif linked_list_len == 0:
            print("Cannot insert data at the given location as the linked list is empty")
        elif location == 0:
            self.head = Node(data, self.head)
        else:
            iteration_object = self.head
            iteration_count = 0
            while iteration_object:
                if iteration_count == (location - 1):
                    iteration_object.next = Node(data, iteration_object.next)
                    return
                iteration_object = iteration_object.next
                iteration_count += 1


    def check_element_exists_in_linked_list(self, data):
        iteration_obj = self.head
        iteration_count = 0
        while iteration_obj:
            if iteration_obj.data == data:
                print("Element in present in linked list at location {}".format(iteration_count))
                return "YES"
            if iteration_obj.next == None:
                print("Element not present in linked list!")
                return "No"
            iteration_obj = iteration_obj.next
            iteration_count += 1


    def _rev_ll(self, current, previous):
        """ USING RECURSION """
        if current == None:
            self.head = previous
            return

        self._rev_ll(current=current.next, previous=current)
        current.next = previous


    def reversing_the_linked_list(self, current, previous):
        if self.head == None or self.length_of_linked_list() == 1:
            return
        else:
            self._rev_ll(current, previous)


if __name__ == "__main__":
    linked_list_obj = LinkedList()
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.insert_element_at_beginning_in_linked_list(5)
    linked_list_obj.insert_element_at_beginning_in_linked_list(10)
    linked_list_obj.insert_element_at_beginning_in_linked_list(15)
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.insert_element_at_the_end_of_linked_list(20)
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.inserting_element_at_given_location_in_a_linked_list(location=0, data=25)
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.check_element_exists_in_linked_list(20)
    linked_list_obj.check_element_exists_in_linked_list(30)
    linked_list_obj.create_linked_list_for_bulk_input([1, 2, 3, 4, 5])
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.create_linked_list_for_bulk_input(["a", "b", "c", "d", "e"])
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.deleting_an_element_from_linked_list_at_given_index(location=3)
    linked_list_obj.print_all_elements_in_linked_list()
    linked_list_obj.length_of_linked_list()
    linked_list_obj.reversing_the_linked_list(current=linked_list_obj.head, previous=None)
    linked_list_obj.print_all_elements_in_linked_list()