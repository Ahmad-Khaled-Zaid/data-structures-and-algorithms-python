def partition(array, low, high):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quick_sort(array, low, pi - 1)

        quick_sort(array, pi + 1, high)
    return array


if __name__ == "__main__":
    array = [8, 4, 23, 42, 16, 15]
    quick_sort(array, 0, len(array) - 1)

    print(f'Sorted array: {array}')
