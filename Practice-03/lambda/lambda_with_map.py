nums = [1, 2, 3]
doubled = list(map(lambda x: x * 2, nums))

names = ["alice", "bob"]
upper_names = list(map(lambda n: n.upper(), names))

prices = [10, 20, 30]
with_tax = list(map(lambda p: p * 1.2, prices))

strings = ["1", "2", "3"]
ints = list(map(lambda s: int(s), strings))