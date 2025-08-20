def find(search_list: list[int], value: int) -> int:
    """Return index of the value in the sorted list."""
    start = 0
    end = len(search_list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = search_list[mid]

        if mid_value == value:
            return mid
        if mid_value > value:
            end = mid - 1
        else:
            start = mid + 1
            
    raise ValueError("value not in array")
