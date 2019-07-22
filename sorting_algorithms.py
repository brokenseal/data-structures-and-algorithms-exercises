import math


def bubble_sort(arr):
    length = len(arr)

    for item_to_move_index in range(length):
        sliced = arr[0:length-item_to_move_index-1]

        for comparing_item_index in range(len(sliced)):
            if arr[comparing_item_index] > arr[comparing_item_index+1]:
                _swap(arr, comparing_item_index, comparing_item_index+1)
    return arr


def selection_sort(arr):
    length = len(arr)
    for i in range(len(arr)):
        index_to_substitute = i
        for j in range(i, length):
            if arr[j] < arr[index_to_substitute]:
                index_to_substitute = j
        _swap(arr, i, index_to_substitute)
    return arr


def quick_sort(arr, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(arr) - 1

    if low < high:
        partition_index = _partition(arr, low, high)
        quick_sort(arr, low, partition_index-1)
        quick_sort(arr, partition_index+1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            _swap(arr, i, j)
    _swap(arr, i+1, high)
    return i + 1


def _swap(arr, first_index, second_index):
    temp = arr[first_index]
    arr[first_index] = arr[second_index]
    arr[second_index] = temp
