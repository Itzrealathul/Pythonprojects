amount=int(input("Enter the amount in dollars: "))
note_1=amount // 1000
note_2=(amount% 1000) //100
note_3=((amount% 1000) %100)//50
note_4=(((amount% 1000)%100)%50)//10
note_5=((((amount% 1000)%100)%50)%10)//5
print("Number of 1000 dollar notes:", note_1)
print("Number of 100 dollar notes:", note_2)
print("Number of 50 dollar notes:", note_3)
print("Number of 10 dollar notes:", note_4)
print("Number of 5 dollar notes:", note_5)
