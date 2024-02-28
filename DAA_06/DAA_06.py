import random
import time
import numpy as np
import matplotlib.pyplot as plt

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]
    return quicksort_random(smaller) + equal + quicksort_random(larger)

def quicksort_non_random(arr):
    if len(arr) <= 1:
        return arr
    
    stack = [(0, len(arr) - 1)]
    while stack:
        low, high = stack.pop()
        pivot = arr[low]
        left, right = low, high
        while left <= right:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        if low < right:
            stack.append((low, right))
        if left < high:
            stack.append((left, high))
    return arr



def generate_input_best_case(n):
    return list(range(n))

def generate_input_worst_case(n):
    return list(range(n, 0, -1))

def generate_input_average_case(n):
    return list(np.random.randint(0, 100, size=n))

def benchmark_quicksort(func, inputs):
    times = []
    for arr in inputs:
        start = time.time()
        func(arr)
        end = time.time()
        times.append(end - start)
    return times

# # Benchmarking
# sizes = [100, 500, 1000, 5000, 10000]
# best_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_best_case(n) for n in sizes])
# worst_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_worst_case(n) for n in sizes])
# average_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_average_case(n) for n in sizes])

# # Plotting
# plt.plot(sizes, best_case_times, label='Best Case')
# plt.plot(sizes, worst_case_times, label='Worst Case')
# plt.plot(sizes, average_case_times, label='Average Case')
# plt.xlabel('Input Size (n)')
# plt.ylabel('Time (seconds)')
# plt.title('Benchmarking Quicksort (Non-Random Pivot)')
# plt.legend()
# plt.show()






# Benchmarking
sizes = [100, 500, 1000, 5000, 10000]

# Run quicksort with random pivot for one example
random_input = generate_input_average_case(10)  # Example input size 10
sorted_random = quicksort_random(random_input.copy())
print("Example of quicksort with random pivot:")
print("Input:", random_input)
print("Output:", sorted_random)
print()

# Run quicksort with non-random pivot for one example
non_random_input = generate_input_average_case(10)  # Example input size 10
sorted_non_random = quicksort_non_random(non_random_input.copy())
print("Example of quicksort with non-random pivot:")
print("Input:", non_random_input)
print("Output:", sorted_non_random)
print()

# Benchmarking
best_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_best_case(n) for n in sizes])
worst_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_worst_case(n) for n in sizes])
average_case_times = benchmark_quicksort(quicksort_non_random, [generate_input_average_case(n) for n in sizes])

# Plotting
plt.plot(sizes, best_case_times, label='Best Case')
plt.plot(sizes, worst_case_times, label='Worst Case')
plt.plot(sizes, average_case_times, label='Average Case')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Benchmarking Quicksort (Non-Random Pivot)')
plt.legend()
plt.show()

