This mini application uses the sounddevice library to take voice input from a user and store it in a file the user names. There is also a simple UI made with PyQT5 which is what I was experiementing with when working on this app.

I used a few functions and classes to handle different aspects of the app. One class handled the main UI and its widgets, while another class took care of the dialog boxes that would pop up.
The createWindow() function created an instance of the main UI class and displayed it to the user. This function was called within the main function for the app. Lastly, the recordAudio() function was used to record the sound needed for the sound file. 

Overall, this was not that difficult of a project. To be honest, the most difficult part was trying to get the PyQT5 UI to work properly. Specifically the dialog boxes closing properly once the user clicked certain buttons.
