from random import randint
import time

def create_list(size, max):
    return [randint(0,max) for integer in range(0, size)]


def create_sorted_list(size):
    return [integer for integer in range(0, size)]


# Bubble sort without nested for loops
def bubble_sort_1(unsorted_list):
    max_length = len(unsorted_list) -1
    sorted = False
    while not sorted:
        sorted = True
        for index in range(0, max_length):
            if unsorted_list[index] > unsorted_list[index+1]:
                sorted = False
                unsorted_list[index], unsorted_list[index+1] = unsorted_list[index+1], unsorted_list[index]
    return unsorted_list


# Bubble sort with nested for loops
def bubble_sort_2(unsorted_list):
    max_length = len(unsorted_list) -1
    for i in range(0, max_length-1):
        for j in range(0 ,i):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list

if __name__ == "__main__":
    # # Random Unsorted List
    input_list =  create_list(10000, 100)
    # #print(input_list)

    # Already sorted list
    # input_list = create_sorted_list(10000)
    #print(input_list)

    t0 = time.time()
    sorted_list_1 = bubble_sort_1(input_list)
    t1 = time.time()
    #print("Sorted List -- {}, Time Taken -- {}".format(sorted_list_1, t1-t0))
    print("Time Taken: {}".format(t1-t0))

    t2 = time.time()
    sorted_list_2 = bubble_sort_2(input_list)
    t3 = time.time()
    #print("Sorted List -- {}, Time Taken -- {}".format(sorted_list_2, t3-t2))
    print("Time Taken: {}".format(t3 - t2))
