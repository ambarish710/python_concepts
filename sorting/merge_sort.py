import random


def create_array(size, max):
    return [random.randint(0, max) for num in range(0, size)]


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
    array = create_array(10, 100)
    print(array)
    sorted_array = merge_sort(array)
    print(sorted_array)
