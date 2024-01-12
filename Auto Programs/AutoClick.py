# Imports the time library
import time
# Imports the threading library which is used to help control and manage clicks
import threading
# Imports button and controller from pynput to take care of mouse input
from pynput.mouse import Button, Controller

# Imports listener and keycode to take care of keyboard input
from pynput.keyboard import Listener, KeyCode

# Sets the delay for when each click should occur
delay = 0.1
# Sets the button to be clicked to right click
button = Button.left
# Sets the start key to c. So when the c key is pressed, the auto clicker starts
start_key = KeyCode(char='c')
# Sets the stop key to b. So when the b key is pressed, the auto clicker stop and exit the appc
stop_key= KeyCode(char='b')

# Class that is used to extend and handle actions related to the threading
class ClickMouse(threading.Thread):

    # Initializer method. Creates running and program_running variables which help handle the clicking loop alongside the start/stop keys
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    # Method to tell the click loop to start. Changes the running value which is used to tell the clicking to start running
    def start_clicking(self):
        self.running = True

    # Method to tell the click loop to stop. Changes the running value which is used to tell the clicking to stop running
    def stop_clicking(self):
        self.running = False

    # Method to tell the clicks to stop
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Method that holds the logic to run the loop.
    def run(self):
        # While the program_running variable is true, then the loop will run
        while self.program_running:
            # While the running variable is true, then the loop will run and the mouse will click the assigned click button
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)




# Instance for the mouse controller class is created so that mouse clicks can be handled
mouse = Controller()
# Instance for the ClickMouse class is made with the delay and specified button passed in
click_thread = ClickMouse(delay, button)
# Starts the thread
click_thread.start()


# Function used to handle the keys being pressed by the user
def on_press(key):
    if key == start_key:
        # If the clicker is already running, this will then pause it
        if click_thread.running:
            click_thread.stop_clicking()
        # If the clicker is not already running, then this will start it
        else:
            click_thread.start_clicking()


    # If the key pressed equals the stop_key, then the clicking stops and the program stops executing
    elif key == stop_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()