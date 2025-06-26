attendance=input("Enter your attedance of class:")
medical_cause=input("Did you have meadical cause?")
if attendance>=75:
    print("You are allowed to attend the exam")

else:
    if(medical_cause=='y'or medical_cause=='Y'):
        print("You are allowed to attend the exam")
    
    else:
        print("You are not allowed")