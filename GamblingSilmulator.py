import random

def main():
    numberOfBets = 0
    numberOfWins = 0
    try:
        stake = int(input("Enter Stake Amount"))
        goal = int(input("Enter Goal Amount"))
    except ValueError:
        print("Please provide valid details!")
    else:
        play(stake, goal, numberOfBets, numberOfWins)        

def play(stake, goal, numberOfBets, numberOfWins):
    playerChoice = 1
    randomNumber = round(random.random())
    
    if check_end_condition(stake, goal):
        print_results(stake, goal, numberOfBets, numberOfWins)
        return
    if randomNumber == 1:
        stake+=1 
        numberOfWins+=1
    else:
        stake-=1
    numberOfBets+=1
    play(stake, goal, numberOfBets, numberOfWins)

def check_end_condition(stake, goal):
    if(stake>=goal or stake==0):
        return True;    
  
def print_results(stake, goal, numberOfBets, numberOfWins):
    print("You won, Stake = "+str(stake) if stake!=0 else "You lost, Stake = "+str(stake))
    print(f'Total number of Bets: {numberOfBets}')
    print(f'Total number of Wins: {numberOfWins}')
    print(f'Average win rate: {(numberOfWins/numberOfBets)*100}')
  

main()