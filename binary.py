decimal_number = int(input("Enter a decimal number: "))
original_number = decimal_number
binary_result = ""

if decimal_number == 0:
    binary_result = "0"
else:
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_result = str(remainder) + binary_result
        decimal_number = decimal_number // 2

print(f"Binary representation of {original_number} is: {binary_result}")