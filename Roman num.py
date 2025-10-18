class RomanConverter:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""
        num = self.number
        for i in range(len(val)):
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
        return roman

# Example use:
number = int(input("Enter an integer: "))
converter = RomanConverter(number)
print("Roman numeral:", converter.to_roman())