def matchwords(word):
    count=0
    list=[]
    for i in word:
        if len(i)>1 and i[0]==i[-1]:
            count=count+1
            list.append(i)
    print("The list of words with same first and last letter",list)
    return count
l=matchwords(["ABC","Hi I am in codingal","SOS","HI"])
print("Number of words having fist and last letter same",l)
    
    