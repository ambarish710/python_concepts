import random
import time


def create_array(size, max):
    return [random.randint(0, max) for number in range(0, size)]


def create_sorted_list(size):
    return [integer for integer in range(0, size)]


def quicksort(array):
    if len(array) <= 1:
        return array
    smaller, equal, larger = [], [], []
    pivot = array[random.randint(0, len(array)-1)]

    for element in array:
        if element > pivot:
            larger.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            smaller.append(element)

    return quicksort(smaller)+equal+quicksort(larger)


if __name__ == "__main__":
    # # Random Unsorted List
    #input_list =  create_array(10000, 100)
    #print("Original Array: {}".format(input_list))

    # Already sorted list
    input_list = create_sorted_list(10000)
    # print(input_list)

    t0 = time.time()
    sorted_array = quicksort(input_list)
    t1 = time.time()
    #print("Sorted List -- {}, Time Taken -- {}".format(sorted_array, t1 - t0))
    print("Time Taken: {}".format(t1-t0))
