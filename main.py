class person(object):
    def __init__(self,name,id_number):
        self.name=name
        self.idnumber=id_number
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(person):
    def __init__(self, name, id_number,salary,post):
        self.salary=salary
        self.post=post
        person.__init__(self,name,id_number)
a=employee("Rahul",18021,2000,"internt")
a.display()