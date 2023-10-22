#This is a simple CLI RPS game.
#This mini-application will be apart of a series of python applications I am building as practice.


#Rock Paper Scissors Game!


import random
import os
import re

totUserScore = [0]
totOppScore = [0]

def CheckGameStatus():
   validChoices = ['y', 'n']
   
   while True:
        try:
            choice = input('Do you want to play again? (Enter Y/N): ')
      
            if choice.lower() not in validChoices:

                raise ValueError('Please input y or n. Nothing else for this part.')
      
            if choice.lower() == 'y':
                return True
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear') #Clears the terminal screen being used for the os
                
                print(f'Here was the final score between us: {totUserScore[0]} : {totOppScore[0]}')
                print('')
                print('Thanks for playing! Now get on out of here!')
                exit()
                
        except ValueError as err:
            print(err)
            
def GameStart():

    userScore = 0
    computerScore = 0    

    isPlaying = True
    
    while isPlaying:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Classic RPS: Rock, Paper, Scissors!')
        
        userChoice = input('Pick your poison - Rock, Paper, or Scissors: ')
        print('')
        
        print(f'Your choice was: {userChoice}')
        print('')
        
        validGameChoices = ['rock', 'paper', 'scissors']
        
        OpponentChoice = random.choice(validGameChoices)
        
        print(f'The computer, (me), chose: {OpponentChoice}')
        print('')
        
        if OpponentChoice == userChoice.lower():
            print('This round is a draw!')
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            isPlaying = CheckGameStatus()
            
        elif OpponentChoice == 'rock' and userChoice == 'scissors':
            print('I win this round! I went rock and you chose scissors!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore

            isPlaying = CheckGameStatus()

        elif OpponentChoice == 'scissors' and userChoice == 'paper':
            print('I win this round! I went scissors and you chose paper!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore

            isPlaying = CheckGameStatus()    
            
        elif OpponentChoice == 'paper' and userChoice == 'rock':
            print('I win this round! I went paper and you chose rock!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore
            
            isPlaying = CheckGameStatus()
            
        else:
            print('Looks like you have won this round.... I guess it is okay to lose sometimes...')
            
            userScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')

            totUserScore[0] = userScore      

            isPlaying = CheckGameStatus()
            
        


if __name__ == '__main__':
   GameStart()
