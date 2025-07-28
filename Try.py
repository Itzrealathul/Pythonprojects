try:
    n=int(input("Enter a number:"))
    print("Number entered is",n)
except ValueError as ex:
    print("Exeption is",ex)
    
    