def reverse_array(original_array):
    if len(original_array) == 0:
        return "list is empty"
    else:
        new_array = []
    i = array_length(original_array)
    x = 1
    while i >= 0:
        new_array += [original_array[i]]
        i -= 1
    return new_array


def array_length(array):
    counter = 0
    for i in array:
        counter += 1
    return counter - 1


print(reverse_array([10, 12, 4, 23, 42, 23, 23]))
