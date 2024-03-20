def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, i):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == i:
            return arr[pivot_index]
        elif pivot_index < i:
            return quickselect(arr, pivot_index + 1, high, i)
        else:
            return quickselect(arr, low, pivot_index - 1, i)

def ith_order_statistic(arr, i):
    n = len(arr)
    if i < 0 or i >= n:
        return None
    return quickselect(arr, 0, n - 1, i)

# Example usage
arr = [3, 2, 1, 5, 4]
i = 2
print(f"The {i}th order statistic is:", ith_order_statistic(arr, i))
