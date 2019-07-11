def binary_search(arr, value_to_search):
    current = sorted(arr)
    length = len(current)
    iterations_count = 0

    while length != 0:
        iterations_count += 1
        mid_index = int(length / 2)
        mid_value = current[mid_index]

        if mid_value == value_to_search:
            return True, iterations_count
        elif mid_value < value_to_search:
            current = current[mid_index+1:]
        else:
            current = current[:mid_index]
        length = len(current)
    return False, iterations_count
