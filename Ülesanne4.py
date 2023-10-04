def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return "Täisarvu ei leitud"

sorted_list = [1, 3, 5, 7, 9, 11, 13]
target_number = 7

result = binary_search(sorted_list, target_number)
print(result)
