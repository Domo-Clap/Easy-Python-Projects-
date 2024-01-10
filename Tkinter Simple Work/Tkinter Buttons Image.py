from tkinter import *
from tkinter.ttk import *

root = Tk()

# Sets the title of the window
root.title('Very, very basic title')

# Sets the size of the window
root.geometry('450x300')

label1 = Label(root, text = 'Image in a Button', font=('Verdana', 14))
label1.grid(row=0, column=4)

photo = PhotoImage(file = r'A:\Pokéwalker.png')

photoImage = photo.subsample(3, 3)

# Create a Button with image only
# btn = Button(root, text='Click me !', image=photo, command=root.destroy)
# btn.grid(row=1, column=3, padx=100)

# Create a Button with image and text
btn2 = Button(root, text='Click me !', image=photoImage, command=root.destroy)
btn2.grid(row=1, column=4, padx=100)

root.mainloop()