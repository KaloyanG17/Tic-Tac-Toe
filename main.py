from random import *

global board
board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

def drawBoard():
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print('---+---+---')
    print(' ' + board[4] + " | " + board[5] + " | " + board[6])
    print('---+---+---')
    print(' ' + board[7] + " | " + board[8] + " | " + board[9])
    print("\n")

def playBoard(position,player):
    board[position] = player

def firstPlayer():
    players = ["O" , "X"]
    shuffle(players)
    return(players)

def aiPlay():
    temp = []
    for i in board.copy():
        flagCheck = True
        try:
            int(board[i])
        except ValueError:
            flagCheck = False
        if flagCheck == True:
            if int(board[i]) == i:
                temp.append(i)
    
    aiChoose =  sample(temp , 1) 
    return(aiChoose[0])

def swapPlayer(playersList):
    temp1 = playersList[0]
    temp2 = playersList[1]
    swappedList = [temp2 , temp1]
    return(swappedList)

def checkWin():
    flagWin = False
    if board[1] == board[2] == board[3]:
        print(board[1], " WINS!!!")
        flagWin = True
    if board[4] == board[5] == board[6]:
        print(board[4], " WINS!!!")
        flagWin = True
    if board[7] == board[8] == board[9]:
        print(board[7], " WINS!!!")
        flagWin = True
    if board[1] == board[5] == board[9]:
        print(board[1], " WINS!!!")
        flagWin = True
    if board[7] == board[5] == board[3]:
        print(board[7], " WINS!!!")
        flagWin = True
    if board[1] == board[4] == board[7]:
        print(board[7], " WINS!!!")
        flagWin = True
    if board[2] == board[4] == board[8]:
        print(board[2], " WINS!!!")
        flagWin = True
    if board[3] == board[6] == board[9]:
        print(board[3], " WINS!!!")
        flagWin = True
    if flagWin == True:
        return(flagWin)



if __name__ == "__main__":

    flagPlayer = False
    while flagPlayer == False:
        start = input("Which player do you want to be? (X/O): ")
        if start == "x" or start == "X":
            sign = "X"
            flagPlayer = True
        if start == "o" or start == "O":
            sign = "O"
            flagPlayer = True
        else:
            print("---ERROR---PLEASE---SELECT---X---OR---Y---")
            
    print("\n" , "You are playing as : " , sign , "\n")
    first = firstPlayer()
    print(first[0] , " is going first!" , "\n")
    counter = 0
    while counter < 9:
        if first[0] == sign:
            drawBoard()
            flagInt = True
            try:
                plays = int(input("Select the position to play: "))
                print("\n")
            except ValueError:
                flagInt = False
                print("THAT IS NOT A POSITION")
            if plays < 10 and plays > 0:
                if flagInt == True:
                    playBoard(plays, first[0])
                    first = swapPlayer(first)
            else:
                print("THAT IS NOT A POSITION")
        else:
            print("---AI---PLAYED---" , "\n")
            playBoard(aiPlay(), first[0])
            first = swapPlayer(first) 
        checks = checkWin()    
        if checks == True:
            break
        counter = counter + 1
    print("\n" , "GAME FINISHED" , "\n")
    drawBoard()