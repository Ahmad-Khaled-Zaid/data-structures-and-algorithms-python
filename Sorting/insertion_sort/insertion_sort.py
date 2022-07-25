def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        temp = arr[i]

        while j >= 0 and temp < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp
    return arr

#
# if __name__ == '__main__':
#     print(insertion_sort([20, 18, 12, 8, 5, -2]))
