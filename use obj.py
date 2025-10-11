class a:
    def __init__(self):
        self.a=a
    def __lt__(self,other):
        if (self.a<other.a):
            return "ob1 is leass than ob2"
        else:
            return "ob2 is leass than ob1"
    def __eq__(self,other):
        if (self.a==other.a):
            return "ob1 is equal to ob2"
        else:
            return "Both are not equal"
ob1=a(3)
ob2=a(5)
print("passed values",ob1.a,ob2.a) 
print(ob1<ob2)
ob3=a(3)
ob4=a(5)
print("passed values",ob3.a,ob4.a) 
print(ob3==ob4)
