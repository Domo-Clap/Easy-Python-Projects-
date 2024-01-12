# Imports the time library
import time
# Imports the threading library which is used to help control and manage clicks
import threading
# Imports controller from pynput to take care of keyboard control
from pynput.keyboard import Controller

# Imports listener and keycode to take care of keyboard input
from pynput.keyboard import Listener, KeyCode


# Sets the delay for when each press should occur
delay = 0.1

# Sets the key to press automatically
keyToAuto = KeyCode(char='w')

# Sets the start key to c. So when the c key is pressed, the auto key presser starts
start_key = KeyCode(char='c')
# Sets the stop key to b. So when the b key is pressed, the auto key presser stops and exits the app
stop_key= KeyCode(char='b')

# Class that is used to extend and handle actions related to the threading
class ClickKey(threading.Thread):

    # Initializer method. Creates running and program_running variables which help handle the pressing loop alongside the start/stop keys
    def __init__(self, delay, keyToPress):
        super(ClickKey, self).__init__()
        self.delay = delay
        self.key = keyToPress
        self.running = False
        self.program_running = True

    # Method to tell the pressing key loop to start. Changes the running value which is used to tell the pressing to start running
    def start_pressing(self):
        self.running = True

    # Method to tell the pressing key loop to stop. Changes the running value which is used to tell the pressing to stop running
    def stop_pressing(self):
        self.running = False

    # Method to tell the key pressing to stop
    def exit(self):
        self.stop_pressing()
        self.program_running = False

    # Method that holds the logic to run the loop.
    def run(self):
        # While the program_running variable is true, then the loop will run
        while self.program_running:
            # While the running variable is true, then the loop will run and the keyboard will press the assigned key
            while self.running:
                # Presses the specified key
                keyboard.press(self.key)
                time.sleep(self.delay)
                # Releases the specified key
                keyboard.release(self.key)
                time.sleep(self.delay)
            time.sleep(0.1)


# Instance for the keyboard controller class is created so that keyboard presses can be handled
keyboard = Controller()
# Instance for the ClickKey class is made with the delay and specified key passed in
click_thread = ClickKey(delay, keyToAuto)
# Starts the thread
click_thread.start()


def on_press(key):
    if key == start_key:
        # If the key presser is already running, this will then pause it
        if click_thread.running:
            click_thread.stop_pressing()
        # If the key presser is not already running, then this will start it
        else:
            click_thread.start_pressing()


    # If the key pressed equals the stop_key, then the key pressing stops and the program stops executing
    elif key == stop_key:
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()