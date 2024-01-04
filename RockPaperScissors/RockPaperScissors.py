#This is a simple CLI RPS game.
#This mini-application will be apart of a series of python applications I am building as practice.


#Rock Paper Scissors Game!


import random
import os
import re

# Total user score
totUserScore = [0]

# Total opponent score
totOppScore = [0]

# Function used to Check the current game status based upon the user's input
def CheckGameStatus():

   # Creates a list of valid options for the user input
   validChoices = ['y', 'n']

   # While loop that runs until it is broken out of
   while True:
        try:
            # Gets user input on whether they want to play the game or not
            choice = input('Do you want to play again? (Enter Y/N): ')

            # If the user input is not in the list of valid choices, then an error is raised and the loop restarts
            if choice.lower() not in validChoices:

                raise ValueError('Please input y or n. Nothing else for this part.')

            # If the user input is Y or y, then True is returned and the loop will run again when needed
            if choice.lower() == 'y':
                return True

           # If the user input is not Y or y, then the program stops executing
            else:
                os.system('cls' if os.name == 'nt' else 'clear') #Clears the terminal screen being used for the os
                
                print(f'Here was the final score between us: {totUserScore[0]} : {totOppScore[0]}')
                print('')
                print('Thanks for playing! Now get on out of here!')
                exit()

        # Catches errors related to input 
        except ValueError as err:
            print(err)

# Function that holds the main game logic
def GameStart():

    # User score initialized to 0
    userScore = 0
    # Opponent score initialized to 0
    computerScore = 0    

    # Used to determine if the game is being played for the while loop
    isPlaying = True

    # While loop that runs until a user says they do not want to play anymore
    while isPlaying:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('')
        print('Classic RPS: Rock, Paper, Scissors!')

        # Gets user input for either rock, paper, or scissors
        userChoice = input('Pick your poison - Rock, Paper, or Scissors: ')
        print('')

        # Reiterates user choice
        print(f'Your choice was: {userChoice}')
        print('')

        # List holding valid choices
        validGameChoices = ['rock', 'paper', 'scissors']

        # Gets a valid choice from the list above and makes it the CPU's choice
        OpponentChoice = random.choice(validGameChoices)

        # States what the user selected, and what the CPU selected
        print(f'The computer, (me), chose: {OpponentChoice}')
        print('')

        # If the user choice and CPU choice are the same, then it is a draw. The is isPlaying variable is then assigned to the result of the CheckGameStatus call
        if OpponentChoice == userChoice.lower():
            print('This round is a draw!')
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            isPlaying = CheckGameStatus()

        # If the user choice is scissors and CPU choice is rock, then the CPU wins. 
        # +1 is added to the computerScore
        # The is isPlaying variable is then assigned to the result of the CheckGameStatus call
        elif OpponentChoice == 'rock' and userChoice == 'scissors':
            print('I win this round! I went rock and you chose scissors!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore

            isPlaying = CheckGameStatus()

        # If the user choice is paper and CPU choice is scissors, then the CPU wins. 
        # +1 is added to the computerScore
        # The is isPlaying variable is then assigned to the result of the CheckGameStatus call
        elif OpponentChoice == 'scissors' and userChoice == 'paper':
            print('I win this round! I went scissors and you chose paper!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore

            isPlaying = CheckGameStatus()    

        # If the user choice is rock and CPU choice is paper, then the CPU wins. 
        # +1 is added to the computerScore
        # The is isPlaying variable is then assigned to the result of the CheckGameStatus call
        elif OpponentChoice == 'paper' and userChoice == 'rock':
            print('I win this round! I went paper and you chose rock!')
            
            computerScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')
            
            totOppScore[0] = computerScore
            
            isPlaying = CheckGameStatus()

        # If the user wins any of the rounds, the following will happen. For this branch to run, the CPU cannot win or draw
        # +1 is added to the userScore
        # The is isPlaying variable is then assigned to the result of the CheckGameStatus call
        else:
            print('Looks like you have won this round.... I guess it is okay to lose sometimes...')
            
            userScore += 1
            
            print(f'The current score between us is: {userScore} : {computerScore}')
            print('')

            totUserScore[0] = userScore      

            isPlaying = CheckGameStatus()
            
        


if __name__ == '__main__':
   GameStart()
