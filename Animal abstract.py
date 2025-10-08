from abc import ABC,abstractmethod
class animal (ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print ("I can walk and learn")   
class snake(animal):
    def move(self):
        print("I can crawl and run")
class dog (animal):
    def move(self):
        print("I can bark")
class lion(animal):
    def move(self):
        print("I can roar")
class snake(animal):
    def move(self):
        print("I can crawl and run")
r=human()
r.move()
k=snake()
k.move()
d=dog()
d.move()
l=lion()
l.move()

                                                                                     