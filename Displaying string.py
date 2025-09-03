class IOstring():
    def __init__(self):
        self.str1=" "
    def getstring(self):
        self.str1=input("Enter string:")
    def printstr(self):
        print("Result is",self.str1.upper())
s= IOstring()
s.getstring()
s.printstr()