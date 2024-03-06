import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
import Excel_To_CSV_UI
import CSV_To_Excel_UI

def Hide_Window(window):
    window.withdraw()

# Used to control the switching between the UIs. Takes input from the dropdown box and calls class object instantions
def Switch_UI(main_window, option):
    if (option == "CSV_To_Excel"):
        from CSV_To_Excel_UI import CSV_To_Excel_UI

        Hide_Window(main_window)

        CSV_To_Excel_UI(main_window).show()

    elif (option =="Excel_To_CSV"):
        from Excel_To_CSV_UI import Excel_To_CSV_UI

        Hide_Window(main_window)

        Excel_To_CSV_UI(main_window).show()

    elif (option == "PDF_To_Docx"):
        from PDF_To_Docx_UI import PDF_To_Docx_UI

        Hide_Window(main_window)

        PDF_To_Docx_UI(main_window).show()



# Function used to display the main UI for the main window. Has a few labels and buttons to navigate to the other pages
def Open_Main_UI():

    # Sets the window settings
    main_window = tk.Tk()
    main_window.title("File Converter App")
    main_window.geometry("500x200")

    main_window.config(bg='gray')

    # Basic header label
    headerLabel = Label(text="File Converter", font=('Arial', 18), fg='black', bg='gray')
    headerLabel.pack(padx=10, pady=5)

    # Dropdown box to select conversion type
    options = ["CSV_To_Excel", "Excel_To_CSV", "PDF_To_Docx"]
    selected_option = StringVar(main_window)
    selected_option.set(options[0])
    dropdown = OptionMenu(main_window, selected_option, *options)
    dropdown.pack(padx=10, pady=5)

    # Button to switch to the selected conversion UI
    switch_button = Button(main_window, text="Switch", command=lambda: Switch_UI(main_window, selected_option.get()))
    switch_button.pack(padx=10, pady=5)

    main_window.mainloop()




# Calls the mainUI method to create the window
if __name__ == "__main__":
    Open_Main_UI()