import random
import re

def reset():
    for dummy_positions in range(0,9):
        board.append("-")


def print_board():
    for position, value in enumerate(board):
        print(value ,end=' ') if position not in (2,5) else print(value)
    print()

def first_play():
    input_choice = int(input("Enter toss(0,1): "))
    try:
        if input_choice not in (0,1):
            raise Exception("Please enter valid choice between 1 and 0!")
    except Exception:
            first_play()
    else:    
        compute_turn(input_choice)        

def compute_turn(input_choice):
    global player,computer,turn_flag
    randomNumber = round(random.random())
    if randomNumber==input_choice:
        print("You won the toss!")
        user_choice=input("Please enter X or O!")
        # if user_choice.upper not in ("X","O"):
        #     raise Exception("Please enter valid choice!")
        player = user_choice
        if player == "X":
            computer = "O"
            turn_flag = "player"
        else:
            computer = "X"
    else:
        print("You lost the Toss!")
        computer = random.choice(["X","O"])
        if computer == "X":
            turn_flag = "computer"
            player = "O"
        else:
            player = "X"


def play():
    winner = check_win()
    if winner != "":
        print(winner+ "won!" )
        return 
    global player,computer,turn_flag
    if turn_flag == "player":
        try:
            location = int(input("Enter position"))
            # if not re.search(location,"\d"):
            #     raise Exception("Invalid location!")
        except Exception:
            play()
        else:
            if board[location] == "-":
                board[location] = player
                turn_flag = "computer"
            else:
                print("Please choose another location!") 
        print_board()
        play()
        
    else:
        location = random.randint(0,8)
        if board[location] == "-":
            board[location] = computer
            turn_flag = "player"
            print_board()
        play()

def check_win():
    if check_row()!="": 
        return check_row() 
    if check_column()!="":
        return check_column() 
    if check_diagnols()!="":
        return check_diagnols() 
    return ""


# 0 1 2
# 3 4 5
# 6 7 8


def check_column():
    for columns in range(0,3):
        if board[columns] == board[columns+3] == board[columns+6] and board[columns] != "-":
            return board[columns]
    return ""

def check_row():
    for rows in range(0,8,3):        
        if board[rows] == board[rows+1] == board[rows+2] and board[rows] != "-":
            return board[rows]
    return ""

def check_diagnols():
    diagnols=0
    if board[diagnols] == board[diagnols+4] == board[diagnols+8] and board[diagnols] != "-" :
        return board[diagnols]
    diagnols=2
    if board[diagnols] == board[diagnols+2] == board[diagnols+4] and board[diagnols] != "-" :
        return board[diagnols]
    return ""

board = []
turn_flag=""
player=""
computer=""
winner=""
reset()
print_board()
first_play()
play()
