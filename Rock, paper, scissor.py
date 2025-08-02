import random

while True:
    user = input("Enter a choice (rock, paper, scissors): ").lower()
    actions = ["rock", "paper", "scissors"]
    
    if user not in actions:
        print("Wrong input")
        continue

    computer = random.choice(actions)
    print(f"You chose {user}, computer chose {computer}")

    if user == computer:
        print("It is a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("You win 🏆")
        else:
            print("You lose")
    elif user == "paper":
        if computer == "rock":
            print("You win 🏆")
        else:
            print("You lose")
    elif user == "scissors":
        if computer == "paper":
            print("You win 🏆")
        else:
            print("You lose")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
