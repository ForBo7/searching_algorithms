def linear_search(list, required_element):
    """
    Performs a linear search to find the required element in the provided list
    and return its index. Returns None if not found.
    """
    for element in list:
        if element == required_element:
            return list.index(required_element)
    return None
