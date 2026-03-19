names = ["Ali", "Dias", "Sara"]
scores = [85, 90, 78]

# enumerate
for index, name in enumerate(names):
    print(index, name)

# zip
paired = list(zip(names, scores))
print("Zipped:", paired)