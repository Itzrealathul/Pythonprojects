Theboard={'7':' ','8':' ','9':'','4':'','5':'','6':'','1':'','2':'','3':''}
boardkeys=[]
for key in Theboard:
    boardkeys.append(key)
def printboard (board):
    print (board['7']+'|'+board['8']+'|'+board['9'])
    print ("-+-+-")
    print (board['4']+'|'+board['5']+'|'+board['6'])
    print ("-+-+-")
    print (board['1']+'|'+board['2']+'|'+board['3'])
    print ("-+-+-")
def game():
    turn='X'
    count=0
    for i in range (10):
        printboard(board)  
        print("It's your turn",+turn+"Move to which place?")
        move=input()
        if Theboard[move] =='' :
            Theboard[move]=turn
        else:
            print("The place is already filled")
            continue
        if count>=5:
            if (Theboard['7']==Theboard['8']==Theboard['9']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['4']==Theboard['5']==Theboard['6']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['1']==Theboard['2']==Theboard['3']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['2']==Theboard['5']==Theboard['8']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['3']==Theboard['6']==Theboard['9']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['7']==Theboard['5']==Theboard['3']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['1']==Theboard['4']==Theboard['7']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
        elif (Theboard['1']==Theboard['5']==Theboard['9']!=' '):
                printboard(Theboard)
                print("Game over!")
                print("****",+turn+"won")
                break
    if count==9:
        print("Game over!,it is a tie")    