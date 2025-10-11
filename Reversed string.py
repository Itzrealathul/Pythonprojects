class StringReverse:
    def __init__(self, text):
       self.__text = text
    def reverse_words(self):
        words = self.__text.split()
        reversed_words = " ".join(reversed(words))
        return reversed_words

    def __str__(self):
        return self.reverse_words()
if __name__ == "__main__":
    s = StringReverse("Hello world this is Python")
    print("Original:", "Hello world this is Python")
    print("Reversed:", s)