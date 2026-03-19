from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
mapped = list(map(lambda x: x * 2, nums))

# filter
filtered = list(filter(lambda x: x % 2 == 0, nums))

# reduce
total = reduce(lambda a, b: a + b, nums)

print("Mapped:", mapped)
print("Filtered:", filtered)
print("Reduced sum:", total)