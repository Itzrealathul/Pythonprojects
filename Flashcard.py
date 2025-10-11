class flashcard:
    def __init__(self,word,meaning):
        self.word=word 
        self.meaning=meaning
    def __str__(self):
        return self.word+self.meaning
flash=[]
print("Welcome to flashcard application")
while True:
    word=input("Enter the name u want to see on flashcard")
    meaning=input("Enter the meaning")
    flash.append(flashcard(word,meaning))
    option=int(input("Enter 0 if u wnat to add another flashcard"))
    if(option):
     break
print("ur flash cards are:" )
for i in flash:
    print(i)
    