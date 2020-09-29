import random
import time


def create_array(size, max):
    return [random.randint(0, max) for num in range(0, size)]


def create_sorted_list(size):
    return [integer for integer in range(0, size)]


def merge(array1, array2):
    array1_idx = 0
    array2_idx = 0
    sorted_array = []
    while array1_idx < len(array1) and array2_idx < len(array2):
        if array1[array1_idx] > array2[array2_idx]:
            sorted_array.append(array2[array2_idx])
            array2_idx += 1
        else:
            sorted_array.append(array1[array1_idx])
            array1_idx += 1
    if array1_idx == len(array1):
        sorted_array.extend(array2[array2_idx:])
    else:
        sorted_array.extend(array1[array1_idx:])
    return sorted_array


def merge_sort(array):
    if len(array) <= 1:
        return array

    left, right = merge_sort(array[:int(len(array)/2)]), merge_sort(array[int(len(array)/2):])

    return merge(left, right)


if __name__ == "__main__":
    # # Random Unsorted List
    #input_list = create_array(10000, 100)
    #print(input_list)

    # Already sorted list
    input_list = create_sorted_list(10000)
    # print(input_list)

    t0 = time.time()
    sorted_array = merge_sort(input_list)
    t1 = time.time()
    #print("Sorted List -- {}, Time Taken -- {}".format(sorted_array, t1 - t0))
    print("Time Taken: {}".format(t1-t0))
