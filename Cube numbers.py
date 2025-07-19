def cube(number):
    return (number*number*number)
def bythree(number):
    if number%3==0:
        cube(number)
    else:
        return False
print (bythree(89))
print (bythree(71))

