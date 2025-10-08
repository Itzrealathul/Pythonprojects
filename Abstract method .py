from abc import ABC , abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Pass value:",x)
    def task(self):
        print("we are inside test class task")
class textclass(Absclass):
    def task(self):
        print("we are inside test class task")
testobj=textclass()
testobj.print(100)




    