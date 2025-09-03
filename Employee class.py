class employee:
    def __init__(self):
        print("Employe created")
    def __del__(self):
        print("Disrupted File")
def create_objent():
    print("Making object")
    obj=employee()
    return obj
o=employee()
print("program end")