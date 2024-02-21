class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, idx):
        return (idx - 1) >> 1

    def left(self, idx):
        return (idx << 1) + 1

    def right(self, idx):
        return (idx << 1) + 2

    def build_min_heap(self, arr):
        self.heap = arr[:]
        size = len(self.heap)
        for idx in range(size // 2, -1, -1):
            self.heapify_down(idx)

    def heapify_down(self, idx):
        smallest = idx
        left_idx = self.left(idx)
        right_idx = self.right(idx)
        size = len(self.heap)
        if left_idx < size and self.heap[left_idx] < self.heap[smallest]:
            smallest = left_idx
        if right_idx < size and self.heap[right_idx] < self.heap[smallest]:
            smallest = right_idx
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self.heapify_down(smallest)

    def heapify_up(self, idx):
        while idx > 0 and self.heap[self.parent(idx)] > self.heap[idx]:
            self.heap[idx], self.heap[self.parent(idx)] = self.heap[self.parent(idx)], self.heap[idx]
            idx = self.parent(idx)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

# Example usage:
heap = MinHeap()
heap.build_min_heap([4, 7, 2, 9, 1, 5])
print("Initial min heap:", heap.heap)

heap.insert(3)
print("Heap after inserting 3:", heap.heap)

print("Popping root node:", heap.pop())
print("Heap after popping root node:", heap.heap)
