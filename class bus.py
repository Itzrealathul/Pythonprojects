class vehicle:
    def __init__(self,name,max_speed, mileage):
        self.name=name 
        self.maxspeed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
sb=bus("volvo",180,20)
print("vehicle name",sb.name,"speed",sb.maxspeed,"mileage:",sb.mileage)



        
        
