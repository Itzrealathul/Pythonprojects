attendance=int(input("Enter your attedance of class:"))

if attendance>=75:
    print("You are allowed to attend the exam")

else:
    medical_cause=input("Did you have meadical cause?:")
    if(medical_cause=='y'or medical_cause=='Y'):
        print("You are allowed to attend the exam")
    
    elif(medical_cause=='N'or medical_cause=='n'):
        print("You are not allowed to attend the exam")
    
    else:
        print("INVALID INPUT")

