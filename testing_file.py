def merge_intervals(arr):
    if not arr:
        return []

    # Step 1: Sort intervals by start time
    arr.sort(key=lambda x: x[0])

    # Step 2: Initialize result list with the first interval
    result = [arr[0]]

    for i in range(1, len(arr)):
        # Get the last interval in the result list
        last_interval = result[-1]

        # Check if the current interval overlaps with the last interval
        if arr[i][0] <= last_interval[1]:  # Overlapping condition
            # Merge the intervals by updating the end time
            last_interval[1] = max(last_interval[1], arr[i][1])
        else:
            # No overlap, add the current interval to the result
            result.append(arr[i])

    return result


# Example usage
arr1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
arr2 = [[7, 8], [1, 5], [2, 4], [4, 6]]

print(merge_intervals(arr1))  # Output: [[1, 4], [6, 8], [9, 10]]
print(merge_intervals(arr2))  # Output: [[1, 6], [7, 8]]
