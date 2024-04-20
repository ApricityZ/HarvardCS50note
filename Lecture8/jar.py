class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if isinstance(n, int) and n > 0 and self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Invalid deposit number")

    def withdraw(self, n):
        if isinstance(n, int) and n > 0 and self.size - n >= 0:
            self.size -= n
        else:
            raise ValueError("Invalid withdraw number")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self.any_name

    @size.setter
    def size(self, n):  # 这里的`n`和`self.__init__(para)`中的形参并无干系,而是当对`self.size`属性进行任意赋值操作时,`@size.setter`都会被调用,这里的`n`也仅仅时赋值时等号`=`右边的任意值
        self.any_name = n

def main():
    jar = Jar()
    print(jar)
    jar.deposit(5)
    print(jar)
    jar.withdraw(3)
    print(jar)
    print(jar.capacity)
    Jar(-1)

if __name__ == '__main__':
    main()