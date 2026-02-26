# generators.py

# Example 1: Using iter() and next()
numbers = [10, 20, 30, 40]
iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Example 2: Looping through an iterator
fruits = ["apple", "banana", "cherry"]
fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)


# Example 3: Custom Iterator Class
class Counter:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration


counter = Counter(5)
for num in counter:
    print(num)


# Example 4: Generator function using yield
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)


# Example 5: Generator expression
squares = (x * x for x in range(6))

for square in squares:
    print(square)