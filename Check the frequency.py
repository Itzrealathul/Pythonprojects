test_dictionary= {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
value = 1
frequency = list(test_dictionary.values()).count(value)
print(f"Frequency of value {value}: {frequency}")