student_details={'id1':{'name':['Sara'],'grade':['6'],'subjects':['Science','Math','English']},
                'id2':{'name':['Satvik'],'grade':['4'],'subjects':['Science','Tamil;','English']},
                'id3':{'name':['Pranav'],'grade':['7'],'subjects':['Science','Math','Social studies']}}
result={}
for key,value in student_details.items():
    if value not in result.values():
        result[key]=value
print(result)
        
        



    
    
