import random
playing=True
number=str(random.randint(20,30))
print("I wil guess a number between 20-30 and guess it right✅")
while playing:
    guess=input("Enter Your guess:")
    if number==guess:
        print("You guessed it right")
        break    
    else:
        print ("your guess isn't quite right😔")