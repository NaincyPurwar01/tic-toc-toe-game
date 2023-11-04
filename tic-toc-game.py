# Print the game board state.
def printboard(xstate , zstate):
    zero = 'X' if xstate[0] == 1 else ('O' if zstate[0] == 1 else 0)
    one  = 'X' if xstate[1] == 1 else ('O' if zstate[1] == 1 else 1)
    two = 'X' if xstate[2] == 1 else ('O' if zstate[2] == 1 else 2)
    three = 'X' if xstate[3] == 1 else ('O' if zstate[3] == 1 else 3)
    four = 'X' if xstate[4] == 1 else ('O' if zstate[4] == 1 else 4)
    five = 'X' if xstate[5] == 1 else ('O' if zstate[5] == 1 else 5)
    six = 'X' if xstate[6] == 1 else ('O' if zstate[6] == 1 else 6)
    seven = 'X' if xstate[7] == 1 else ('O' if zstate[7] == 1 else 7)
    eight = 'X' if xstate[8] == 1 else ('O' if zstate[8] == 1 else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")

# Checking who is the Winner.
#Is it 'X'
#Is it 'O'
#Or "Draw" the game.
def checkstate(xstate , zstate):
    winscondition = [[0 , 1 ,2] , [3 , 4 ,5] , [6 , 7 , 8], [0 , 3 , 6] , [1 , 4 , 7] , [2 , 5 , 8] , [0 , 4 , 7] , [2 , 4 ,6]]
    for win in winscondition:
        if(( xstate[win[0]] + xstate[win[1]] + xstate[win[2]]) == 3):
            print(f"X wins the match")
            return 1
        if((zstate[0] + zstate[1] + zstate[2]) == 3):
            print(f"0 wins the match")
            return 0
    return -1


#Main file
#And taking input from the user.
if __name__ == "__main__":
    xstate = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    zstate = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    checkvalues = set()
    turn  = 1 # ! for 'X ' and '0' for 'O'
    print("Welcom to Tic - Toe - Tac Game")
    while(True):
        if(turn == 1):
            print("X 's Chance")
            value = int(input("Please enter a value :"))
            if value in checkvalues:
                print(f"Please modify the values")
                continue
            checkvalues.add(value)
            xstate[value] = 1
        else:
            print("O's chance")
            value = int(input("Please enter a value :"))
            if value in checkvalues:
                print(f"Please modify the values")
                continue
            checkvalues.add(value)
            zstate[value] = 1
        turn = 1 - turn
        check = checkstate(xstate , zstate)
        if check != -1:
            print(f"Match over")
            break
        else:
            count = 0
            count1 = 0
            for x in xstate:
                if x == 'X':
                    count += 1
            for z in zstate:
                if z == 'O':
                    count1 += 1
            if(count == 9):
                print(f"Match is over noone is winner")
                break
            if(count1 == 9):
                print("Match is over Noone is Winner")
                break
        printboard(xstate , zstate)
