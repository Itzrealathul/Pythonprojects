rowSize = int(input("enter the number of rows: "))
if rowSize%2 == 0:
    half=rowSize//2
else:
    half=(rowSize//2+1)
space=half-1
for i in range(1,half+1):
    for j in range(1,space+1):
        print(end=" ")
    space=space-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
        