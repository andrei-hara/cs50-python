class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        if self.size > self.capacity:
            raise ValueError("Too many cookies")

    def withdraw(self, n):
        self.size -= n
        if self.size < 0:
            raise ValueError("Don't have that many cookies in the jar")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Negative capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        self._size = n


def main():
    coockieJar = Jar(7)
    coockieJar.size = 9
    coockieJar.deposit(5)
    coockieJar.withdraw(1)
    print(coockieJar.size)
    print(coockieJar)


if __name__ == "__main__":
    main()