class myclass:
    __privatevar=27
    def __privemeth(self):
        print ("I am in side class my class")
    def hello(self):
        print("Private variable value",myclass.__privemeth)
po=myclass()
po.hello()
po.__privemeth()