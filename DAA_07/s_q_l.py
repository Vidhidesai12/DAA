class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = [0] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1    

    def push(self, value):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.arr[self.top]

# Example usage
stack = Stack(5)
stack.push(1)
stack.push(2)
stack.push(3)
print("Peek:", stack.peek())
print("Pop:", stack.pop())
print("Peek after pop:", stack.peek())
