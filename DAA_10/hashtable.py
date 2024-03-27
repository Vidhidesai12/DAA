class HashNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class CustomLinkedList:
    def __init__(self):
        self.head = None

    def append(self, key, value):
        new_node = HashNode(key, value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove(self, key):
        if not self.head:
            return False
        if self.head.key == key:
            self.head = self.head.next
            return True
        current = self.head
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return True
            current = current.next
        return False

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

class HashMap:
    DEFAULT_CAPACITY = 16
    LOAD_FACTOR = 0.75
    SHRINK_FACTOR = 0.25

    def __init__(self):
        self.bucket_array = [CustomLinkedList() for _ in range(self.DEFAULT_CAPACITY)]
        self.size = 0

    def hash_function(self, key):
        return hash(key) % len(self.bucket_array)

    def insert(self, key, value):
        index = self.hash_function(key)
        self.bucket_array[index].append(key, value)
        self.size += 1
        if self.size > self.LOAD_FACTOR * len(self.bucket_array):
            self.resize(len(self.bucket_array) * 2)

    def retrieve(self, key):
        index = self.hash_function(key)
        return self.bucket_array[index].search(key)

    def delete(self, key):
        index = self.hash_function(key)
        if self.bucket_array[index].remove(key):
            self.size -= 1
            if self.size < self.SHRINK_FACTOR * len(self.bucket_array):
                self.resize(len(self.bucket_array) // 2)

    def resize(self, new_capacity):
        new_bucket_array = [CustomLinkedList() for _ in range(new_capacity)]
        for bucket_list in self.bucket_array:
            current = bucket_list.head
            while current:
                new_index = self.hash_function(current.key)
                new_bucket_array[new_index].append(current.key, current.value)
                current = current.next
        self.bucket_array = new_bucket_array

    def display(self):
        for i, bucket_list in enumerate(self.bucket_array):
            print(f"Bucket {i}: ", end="")
            current = bucket_list.head
            while current:
                print(f"({current.key}, {current.value}) ", end="")
                current = current.next
            print()


hash_map = HashMap()
while True:
    print("Choose an operation:")
    print("1. Insert")
    print("2. Remove")
    print("3. Display Table")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        key = int(input("Enter key: "))
        value = int(input("Enter value: "))
        hash_map.insert(key, value)
    elif choice == '2':
        remove_key = int(input("Enter key to remove: "))
        hash_map.delete(remove_key)
    elif choice == '3':
        hash_map.display()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
