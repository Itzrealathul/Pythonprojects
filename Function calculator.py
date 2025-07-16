def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("A.add")
print("B.subtract")
print("C.divide")
print("D.multiply")
choice=input("Enter your choice:")
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if choice=="A":
    print("The sum is",add (num1,num2))
elif choice=="B":
    print("The difference is",sub (num1,num2))

elif choice=="C":
    print("The division is",divide (num1,num2))

elif choice=="D":
    print("The product is",multiply (num1,num2))

else:
    print("Invalid choice")
    
    