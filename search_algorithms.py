def binary_search(current, value_to_search):
    min_index = 0
    max_index = len(current) - 1

    while min_index <= max_index:
        mid_index = min_index + int((max_index-min_index) / 2)
        mid_value = current[mid_index]

        if mid_value == value_to_search:
            return mid_index

        if mid_value < value_to_search:
            min_index = mid_index+1
        else:
            max_index = mid_index-1
    return -1
