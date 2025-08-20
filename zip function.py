s1={2,3,1}
s2={4,5,6}
s3=list(zip(s1,s2))
print(s3)
l1=[10,20,30,40]
l2=[100,200,300,4000]
for x,y in zip(l1,l2[:-1]):
    print(x,y)
    
    