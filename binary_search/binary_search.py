def binary_search(list, required_element):
    """
    Performs a binary search on the provided list and returns the index of the
    required element. Returns None if not found.
    """
    start_index = 0
    end_index = len(list) - 1
    while True:
        middle_index = (start_index + end_index) // 2
        if list[middle_index] == required_element:
            return middle_index
        elif start_index == end_index:
            break
        elif list[middle_index] < required_element:
            start_index = middle_index + 1
        elif list[middle_index] > required_element:
            end_index = middle_index - 1
    return None
