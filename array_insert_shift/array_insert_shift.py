# function to add a value in the middle of the  array
def insert_shift_array(array, value):
    if type(array) != list:
        return "please pass an list as a first parameter"
    else:
        length = array_length(array)
        mid_index = (length // 2) if length % 2 == 0 else (length // 2) + 1
        array = array[0:mid_index] + [value] + array[mid_index:]
    return array


# function to find the length of the array
def array_length(array):
    counter = 0
    for i in array:
        counter += 1
    return counter


