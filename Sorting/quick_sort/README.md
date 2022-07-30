# Challenge Summary

create a function called quick sort that will take an array and return the array sorted

## Whiteboard Process

![whiteBoard](while%20board%20quick%20sort.png)

## Approach & Efficiency

divide and conquer strategy to divide the array and then merge it while applying sorted algorithm

## Solution

```python
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
```