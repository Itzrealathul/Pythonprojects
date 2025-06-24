Character=input("Enter a character to find if it is a number or Alpahbet ,NO SPECIAL CHARCTER:")
if len(Character)!=1:
    print ("Pls enter only one character")
else:
    if (Character >= 'a' and Character <= 'z') or (Character >= 'A' and Character <= 'Z'):
        print (Character,"is an alphabet")
    elif Character >=0:
        print (Character,"is and digit")
    else:
        print(Character,"is a special charcter")
 
    
  

    
    

    

    
    