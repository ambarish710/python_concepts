import random


def create_array(size, max):
    return [random.randint(0, max) for number in range(0, size)]


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
    array =  create_array(10, 100)
    print("Original Array: {}".format(array))
    sorted_array = quicksort(array)
    print("Sorted Array: {}".format(sorted_array))
