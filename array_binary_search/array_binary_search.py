def binary_search(array, key):
    """
    This function will take a list and key as  parameters, and it will return the  key index,
    if the key is not found , return -1 \n
    :param array:
    :param key:
    :return: the key index or -1
    """
    new_array = sort_array(array)
    print(new_array)
    lower_bound = 0
    upper_bound = len(new_array) - 1
    while lower_bound <= upper_bound:
        mid_index = (lower_bound + upper_bound) // 2
        if new_array[mid_index] == key:
            return mid_index
        if new_array[mid_index] > key:
            upper_bound = mid_index - 1
        else:
            lower_bound = mid_index + 1
    return -1


def sort_array(array):
    """
    This function will take a list as a parameter and return new list ordered in ascending order.\n
    :param array:
    :return: sorted list (ASC)
    """
    new_array = []
    k = 0
    for i in range(0, len(array)):
        minimum = array[0]
        for j in range(0, len(array)):
            if array[j] <= minimum:
                k = j
                minimum = array[j]

        array[k], array[len(array) - 1] = array[len(array) - 1], array[k]
        array = array[0:-1]
        new_array += [minimum]
    return new_array


print(binary_search([-1, 20, 4, 32, 16, 0, 15], 20))
