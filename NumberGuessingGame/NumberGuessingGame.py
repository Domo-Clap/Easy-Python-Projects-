#This is a simple CLI number guessing game.
#This mini-application will be apart of a series of python applications I am building as practice.


#Number Guessing Game!

import random
from tkinter import N

listOfAttempts = []

# Shows the score to the user
def Show_Score():
    # If there are no attempts
    if not listOfAttempts:
        print('No high score in the attempts list')
        print()

    # If there are some attempts
    else:
        print(f'The current high score in the attempts list is: '
              f' {min(listOfAttempts)} attempts')
        print()

# Game Logic Function
def Game_Start():
    # Initializes the number of attempts
    numAttempts = 0
    # Creates a random number from 1 - 10
    rand_num = random.randint(1, 10)

    # Basic welcome text
    print('Hello! Welcome to the Number Guessing Game!')
    print()

    # Used to keep while loop running
    isValidID = False

    # If the isValidID variable is set to true, then the loop will break. Otherwise, the loop will continue to run
    # Used to get a proper ID from the user
    while isValidID == False:    

        # Asks user for their wanted UID
        playerID = input('What do you want your name to be? ')
        print()

        # If the length of the entered UID is less than 1 and greater than 12, then the loop will start over again thanks to the continue statement
        if len(playerID) < 1 or len(playerID) > 12:
            print('Please make sure you enter a proper name!')
            print()
            continue

        # If the lenfth of the entered UID is greater than 1 and less than 12, then the while loop will break and the UID will be saved
        else:
            print(f'Sounds like a great name, {playerID}!')
            print()
            isValidID = True

    # Asks player if they would like to play the game. Waits for Y or N
    playChoice = input(
        f'Hi, {playerID}, would you like to play '
        f'the number guessing game?  (Enter Y/N): ')

    # If the user input is not Y or y, then the code breaks and the app stops executing
    if playChoice.lower() != 'y':
        print('That\'s okay! Thanks anyways!')
        print()
        exit()
    # If the user input is Y or y, then the show_Score function is called.
    else:
        Show_Score()

    # After the show_Score function is called, a while loop is started and the true game logic starts
    while playChoice.lower() == 'y':
        # Try statement used to help catch any input errors
        try:
            # Gets the user input for the guessed number
            userGuess = int(input('Pick a number between 1 and 10: '))
            print()

            # If the number is less than 1 or greater than 10, an error is raised an caught. Then the loop restarts
            if userGuess < 1 or userGuess > 10:
                raise ValueError('Please pick a number between 1 and 10, nothing else.')

            # After the user has guessed a proper number, the numAttempts is increased by 1
            numAttempts += 1
            
            # If the user guess equals the random number stored earlier, then the user is told how many attempts it took.
            # Then the user is asked if they want to play again
            if userGuess == rand_num:
                print('Good Job! You got the right answer!')
                print()
                print(f'It took you {numAttempts} attempts')
                listOfAttempts.append(numAttempts)
                print()
                playChoice = input('Would you like to play again? (Enter Y/N): ')
                print()

                # If the choice to play again is not Y or y, then the game logic loop breaks
                if playChoice.lower() != 'y':
                    print('That\'s okay! Thanks anyways!')
                    break
                # If the choice to play again is Y or y, then the numAttempts is reset to 0 and a new random number is assigned
                else:
                    numAttempts = 0
                    rand_num = random.randint(1, 10)
                    Show_Score()
                    continue

            # If the user guess does not equal the random number stored earlier, then the user is told whether the random number is higher or lower than the guess
            else:
                if userGuess > rand_num:
                    print('A bit too high of a guess')
                elif userGuess < rand_num:
                    print('A bit too low of a guess')

        # Looks for exceptions related to input errors
        except ValueError as err:
            print('Looks like you entered an incorrect value! Please try again!')
            print(err)
            

if __name__ == '__main__':
    Game_Start()



