#Vidhi Desai
class MinHeap:
    def __init__(self):
        # Initialize an empty list to store the elements of the heap
        self.heap = []

    def parent(self, idx):
         # Returns the index of the parent node of the node at index idx
        return (idx - 1) >> 1

    def left(self, idx):
        # Returns the index of the left child of the node at index idx
        return (idx << 1) + 1

    def right(self, idx):
        # Returns the index of the right child of the node at index idx
        return (idx << 1) + 2

    def build_min_heap(self, arr):
        # Builds a min heap from a given array arr
        # Copy the array into the heap
        self.heap = arr[:]
        size = len(self.heap)
        # Start from the last parent node and move up to the root
        for idx in range(size // 2, -1, -1):
            # Heapify down each parent node
            self.heapify_down(idx)

    def heapify_down(self, idx):
        # Fix the min heap property starting from the node at index idx
        smallest = idx
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        size = len(self.heap)
        # Compare the node with its left and right children, if they exist
        if left_idx < size and self.heap[left_idx] < self.heap[smallest]:
            smallest = left_idx
        if right_idx < size and self.heap[right_idx] < self.heap[smallest]:
            smallest = right_idx
        # If the smallest node is not the current node, swap them and continue heapifying down
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.heapify_down(smallest)

    def heapify_up(self, idx):
        # Fix the min heap property starting from the node at index idx and moving upwards
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            # Swap the node with its parent if it violates the min heap property
            self.heap[idx], self.heap[self.parent(idx)] = self.heap[self.parent(idx)], self.heap[idx]
            idx = self.parent(idx)

    def insert(self, item):
        # Insert a new item into the heap
        # Append the item to the end of the heap
        self.heap.append(item)
        # Fix the min heap property by heapifying up from the inserted node
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        # Remove and return the smallest item from the heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        # Remove the root node and replace it with the last node
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        # Fix the min heap property by heapifying down from the root
        self.heapify_down(0)
        return root

# Example usage:
heap = MinHeap()
heap.build_min_heap([9, 8, 7, 6, 5, 4, 3, 2, 1])
print("Initial min heap:", heap.heap)

heap.insert(10)
print("Heap after inserting 10:", heap.heap)

print("Popping root node:", heap.pop())
print("Heap after popping root node:", heap.heap)

