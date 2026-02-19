nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))

words = ["apple", "dog", "banana", "cat"]
long_words = list(filter(lambda s: len(s) > 3, words))

prices = [100, 500, 20, 1500]
expensive = list(filter(lambda p: p > 200, prices))

mixed = [True, False, True, True]
only_true = list(filter(lambda x: x is True, mixed))