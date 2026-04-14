class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies in the jar!")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Size must be non-negative")
        if size > self.capacity:
            raise ValueError("Size must not exceed capacity")
        self._size = size

def main():
    try:
        jar = Jar(12)
        print(f"Empty Jar capacity: {jar.capacity}, size: {jar.size}")
        
        jar.deposit(12)
        print(f"After deposit: {jar}")
        
        jar.withdraw(11) 
        print(f"After withdrawal: {jar}")
        print("cookie.gif")
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()