points = [(1, 2), (4, 1), (5, -1)]
sorted_pts = sorted(points, key=lambda p: p[1])

users = [{"name": "Max", "age": 25}, {"name": "Ann", "age": 20}]
sorted_users = sorted(users, key=lambda u: u["age"])

words = ["banana", "apple", "cherry"]
by_length = sorted(words, key=lambda s: len(s))

data = ["A10", "B2", "C5"]
by_num = sorted(data, key=lambda x: int(x[1:]))