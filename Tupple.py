def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
sample_tuple = (2, 3, 4, 5)
result = tuple_product(sample_tuple)
print("Product of tuple elements:", result)