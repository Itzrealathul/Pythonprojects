n=10
for i in range(n):
    if i % 2==0:
        print("twist")
    elif i % 15==0:
        pass
    elif i % 5 ==0:
        print("Buzz")
    elif i % 3 ==0:
        print("Fuzz")
    else:
        print(i)
        