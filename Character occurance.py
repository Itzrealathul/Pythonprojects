word=input("Enter any word to check:")
char=input("Enter any chracter:")
i=0
count=0
while (i<len(word)):
    if(word[i]==char):
         count=count+1
    i=i+1
print("The number of times",char,"has occured is",count)