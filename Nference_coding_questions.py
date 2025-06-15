def max_subarray_sum(nums):
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global


print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6


def palindrome(string):
    if string == string[::-1]:
        print("The given string is Palindrome")
    else:
        print("The given string is not a Palindrome")


palindrome("racecar")


def find_kth_largest(nums, k):
    nums.sort(reverse=True)  # Sort the array nums in descending order
    return nums[k - 1]  # Return the element at index k-1 (0-based index)


nums = [3, 2, 1, 5, 6, 4]  # Input array
k = 2  # Find the 2nd largest element

print(find_kth_largest(nums, k))  # Output: 5


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([3, 6, 8, 10, 1, 2, 1]))


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1


print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))