#This is another mini-application that will be added to my compilation of small python apps
#This application is pretty much a countdown timer that will get input and count down by the second


#Countdown Timer Application

#Imports the time library which lets you represent time in code.
import time

#Takes the input time from the user as a parameter
def CountDown(inputTime):
    #While the user inputted countdown time is greater than or equal to 0, then this loop will run
    while inputTime >= 0: 
        mins, secs = divmod(inputTime, 60) #Takes two numbers and returns a pair of numbers consisting of their quotient and remainder. 
        timer = '{:02d}:{:02d}'.format(mins, secs) #Assigns the amount of minutes and seconds as a tuple to the timer variable
        
        #Displays the timer every iteration. Prints every 1 second
        print(timer, end='\r')
        time.sleep(1) #Tells the code to stop for 1 second before continuing
        inputTime -= 1
        
    #After the loop ends, aka, when the time reaches -1, a message will be displayed
    print('BZZZZZ! Time is up!')
    

#Start of main function
if __name__ == '__main__':
   
   #Used to determine if loop should continue
   validTimeInput = False
   
   #Asks user for input
   inputTime = int(input("Enter a time in seconds: "))
   
   #While the bool value is false, then the loop continues and the user must enter a value again.
   while validTimeInput == False:
        
        #If the inputTime is greater than 0, then it is valid and the loop breaks
        if inputTime >= 1:
            break
            
        #If the inputTime is less than 1, then the loop continues and the inputTime is invalid.
        else:
            print('That is an invalid time. Countdown amount cannot be 0 or less.')
            validTimeInput = False
            
        inputTime = int(input("Enter a time in seconds: "))

   CountDown(inputTime)
