from random import randint
import os
import sys
from colorama import Fore, Style
#-------------------------------
# Variable
nextRound=True
# Banner
print (Fore.LIGHTBLUE_EX+'*************************************  *************************************************')
print ('**     ****     *****     **  ****  *  **     *****   ********     ***       ***     ***')
print ('*  ***  **  ***  ***  ******  **  ***  *  ***  ***  *  ******  ***  **  *******  ***  **')
print ('*  ***  **  ***  **  *******    *****  *  ***  **  ***  *****  ***  **  *******  ***  **')
print ('*     ****  ***  **  *******    *****  *     ***         ****     ****       **     ****')
print ('*  **  ***  ***  ***  ******  **  ***  *  *****  *******  ***  *******  *******  **  ***')
print ('*  ***  ***     *****     **  ****  *  *  ****  *********  **  *******       **  ***  **')
print ('*************************************  *************************************************'+Style.RESET_ALL)

# Player Name & Welcome Section

print('Welcome to Rock, Paper, Scissors Game.\n')
playerName=input('Please Enter your name : ')
print(Fore.GREEN +(f'\nWelcome {playerName}, Please Read Game Rules')+ Style.RESET_ALL)

# Games Rules

for num in range(1,6,2):
    print(Fore.LIGHTYELLOW_EX+('*' * num))
print('GAME RULES')
print('ROCK can break SCISSORS, so ROCK wins.')
print('SCISSORS can cut PAPER, so SCISSORS wins.')
print('PAPER can cover ROCK, so PAPER wins.')
print(Fore.BLUE+('Use the letter "R" instead of ROCK'))
print('Use the letter "P" instead of PAPER')
print('Use the letter "S" instead of SCISSORS')
for num in range(5,0,-2):
    print(Fore.LIGHTYELLOW_EX+('*' * num)+Style.RESET_ALL)

while nextRound==True:
    totalScore=int(input('\nHow Many rounds must the winner have won ? : '))

# Clear Screen

    if os.name =='nt' :
        os.system('cls')
    else:
        os.system('clear')

# Game Codes
    playerScore=0
    cumScore=0
    print(Fore.GREEN+'Start the Game')
    while playerScore<totalScore and cumScore<totalScore:
        randomNumber=None
        randomNumber = randint(0,5)
        cumPlayer=None
        if randomNumber==0 or randomNumber==5:
            cumPlayer='Rock'
        elif randomNumber==1 or randomNumber==4:
            cumPlayer='Paper'
        elif randomNumber==2 or randomNumber==3:
            cumPlayer='Scissors'
        print(' [ R ] Rock , [ P ] Paper , [ S ] Scissors \n ------------------------------'+Style.RESET_ALL)
# Main Game Codes
        while True:
            playerMove=input('Enter your Choose between [ R , P , S ] : ').lower()
            if playerMove=='r' or playerMove=='p' or playerMove=='s':
                if playerMove=='r':
                    playerMove='Rock'
                elif playerMove=='p':
                    playerMove='Paper'  
                else :
                    playerMove='Scissors'  
                break
            else:
                print(Fore.RED+'Please Enter Corect Word !!!!!'+Style.RESET_ALL)   
            
    
        print(Fore.GREEN+'-------------------------------------------\n')
        print(f'Your Choose :  {playerMove}')
        print(f'Computer Choose : {cumPlayer}\n ') 

        if playerMove==cumPlayer:
            print('Draw')
        elif playerMove=='Rock':
            if cumPlayer=='Paper':
                cumScore+=1
                print('Computer Won')
            else:
                playerScore+=1
                print(f'{playerName} Won')

        elif playerMove == 'Paper':
            if cumPlayer=='Rock':
                playerScore+=1
                print(f'{playerName} Won')
            else:
                cumScore+=1
                print('Computer Won')
        else:
            if cumPlayer=='Rock':
                cumScore+=1
                print('Computer Won')
            else:
                playerScore+=1
                print(f'{playerName} Won')
        print(Fore.GREEN+(f'{playerName} = {playerScore} and Computer = {cumScore}\n')+Style.RESET_ALL)
    if playerScore==cumScore:
        print('The Game Was Tied')
    elif playerScore>cumScore:
        print(Fore.BLUE+(f'{playerName} Wins The Game\n')+Style.RESET_ALL)
    else:
        print(Fore.BLUE+'Computer Wins The Game\n'+Style.RESET_ALL)
    print(Fore.RED+'Do you want play game again ?'+Style.RESET_ALL)
    again = input('Yes  or  No   :   ').lower()
    if again=='yes' or again =='y':
        nextRound=True
    else:
        nextRound=False



