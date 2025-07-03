num=int(input("Enter a number:")
temp=num
while num>0:
    digit=num % 10
    num=num//10
    sum=sum+digit**3
if (temp==sum):
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")