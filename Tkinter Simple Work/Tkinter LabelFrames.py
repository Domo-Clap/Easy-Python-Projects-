from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

# Creates a new label frame widget
label_frame = LabelFrame(root, text='This is a Label Frame')
label_frame.pack(expand='yes', fill='both')

# Creates a new label to go in the label frame
label1 = Label(label_frame, text='1. First label.')
# Places the label
label1.place(x = 0, y = 5)

# Creates a new label to go in the label frame
label2 = Label(label_frame, text='2. Second label.')
# Places the label
label2.place(x = 0, y = 35)

# Creates a new label to go in the label frame
label3 = Label(label_frame, text='3. Third label.')
# Places the label
label3.place(x = 0, y = 65)

# Creates a button to go in the label frame
btn1 = Button(label_frame, text='Click Me!')
# Places the button
btn1.place(x = 200, y = 95)

# Creates a check button to go in the label frame
chkBtn = Checkbutton(label_frame, text='Maybe this one?')
# Places the check box
chkBtn.place(x = 200, y = 135)

# Starts the main window and displays it
root.mainloop()