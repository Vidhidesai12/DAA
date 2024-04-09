#Vidhi Desai
#1002081553
class DynamicArray:
    def __init__(self):
        self.data = []
        self.size = 0

    def push_back(self, value):
        self.data.append(value)
        self.size += 1

    def at(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def pop_back(self):
        if self.size > 0:
            self.data.pop()
            self.size -= 1

    def __len__(self):
        return self.size

# Example usage:
if __name__ == "__main__":
    dynamic_array = DynamicArray()

    dynamic_array.push_back(1)
    dynamic_array.push_back(2)
    dynamic_array.push_back(3)

    print("Element at index 1:", dynamic_array.at(1))  # Should print 2

    dynamic_array.pop_back()
    print("Size after pop:", len(dynamic_array))  # Should print 2
class DynamicArray:
    def __init__(self):
        self.data = []
        self.size = 0

    def push_back(self, value):
        self.data.append(value)
        self.size += 1

    def at(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        else:
            raise IndexError("Index out of range")

    def pop_back(self):
        if self.size > 0:
            self.data.pop()
            self.size -= 1

    def __len__(self):
        return self.size


if __name__ == "__main__":
    dynamic_array = DynamicArray()

    print("Interactive DynamicArray Program")
    while True:
        print("\nOptions:")
        print("1. Push element to the back")
        print("2. Access element by index")
        print("3. Pop element from the back")
        print("4. Print current array")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            value = int(input("Enter the value to push: "))
            dynamic_array.push_back(value)
            print("Element pushed to the back.")

        elif choice == '2':
            index = int(input("Enter the index to access: "))
            try:
                element = dynamic_array.at(index)
                print("Element at index", index, ":", element)
            except IndexError as e:
                print(e)

        elif choice == '3':
            dynamic_array.pop_back()
            print("Element popped from the back.")

        elif choice == '4':
            print("Current array:", dynamic_array.data)

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
