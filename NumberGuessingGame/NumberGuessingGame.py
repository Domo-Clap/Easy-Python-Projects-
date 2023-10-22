#This is a simple CLI number guessing game.
#This mini-application will be apart of a series of python applications I am building as practice.


#Number Guessing Game!

import random
from tkinter import N

listOfAttempts = []

def Show_Score():
    if not listOfAttempts:
        print('No high score in the attempts list')
        print()
        
    else:
        print(f'The current high score in the attempts list is: '
              f' {min(listOfAttempts)} attempts')
        print()


def Game_Start():
    numAttempts = 0
    rand_num = random.randint(1, 10)
    
    print('Hello! Welcome to the Number Guessing Game!')
    print()
    
    isValidID = False
    
    while isValidID == False:    

        playerID = input('What do you want your name to be? ')
        print()
    
        if len(playerID) < 1 or len(playerID) > 12:
            print('Please make sure you enter a proper name!')
            print()
            continue
            
        else:
            print(f'Sounds like a great name, {playerID}!')
            print()
            isValidID = True
    
    playChoice = input(
        f'Hi, {playerID}, would you like to play '
        f'the number guessing game?  (Enter Y/N): ')
    
    if playChoice.lower() != 'y':
        print('That\'s okay! Thanks anyways!')
        print()
        exit()
    
    else:
        Show_Score()
    
    while playChoice.lower() == 'y':
        try:
            userGuess = int(input('Pick a number between 1 and 10: '))
            print()
            
            if userGuess < 1 or userGuess > 10:
                raise ValueError('Please pick a number between 1 and 10, nothing else.')
            
            numAttempts += 1
            
            
            if userGuess == rand_num:
                print('Good Job! You got the right answer!')
                print()
                print(f'It took you {numAttempts} attempts')
                listOfAttempts.append(numAttempts)
                print()
                playChoice = input('Would you like to play again? (Enter Y/N): ')
                print()
                
                if playChoice.lower() != 'y':
                    print('That\'s okay! Thanks anyways!')
                    break
                else:
                    numAttempts = 0
                    rand_num = random.randint(1, 10)
                    Show_Score()
                    continue
                
            else:
                if userGuess > rand_num:
                    print('A bit too high of a guess')
                elif userGuess < rand_num:
                    print('A bit too low of a guess')
             
        except ValueError as err:
            print('Looks like you entered an incorrect value! Please try again!')
            print(err)
            

if __name__ == '__main__':
    Game_Start()



