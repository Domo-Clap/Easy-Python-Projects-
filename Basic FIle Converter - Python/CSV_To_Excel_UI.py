# Imports tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import pandas as pd


class CSV_To_Excel_UI:

    # Function that opens up a file dialog box and gets the user to select a csv file
    # If the file path is valid, it will change the csvEntry value accordingly
    def choose_csv(self):

        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        if file_path:
            self.csvEntry.delete(0, END)
            self.csvEntry.insert(0, file_path)

    # Function used to convert a csv file to an excel file
    # Takes the file selected by the user and uses pandas to convert it to an excel file
    def convert_csv_to_excel(self):

        # Gets the file path from the csvEntry box
        csv_file_path = self.csvEntry.get()

        # If the csv file path is valid then it will try to change it to an excel file where the user specifies the file path
        if csv_file_path:
            try:
                df = pd.read_csv(csv_file_path)
                excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])

                # If the excel file path chosen is valid, then the file will be converted, and it will show a messagebox
                if excel_file_path:
                    df.to_excel(excel_file_path, index=False)
                    messagebox.showinfo("Success", f"CSV file f'{csv_file_path}' has been successfully converted to Excel files '{excel_file_path}'")
                # Otherwise, a warning message box will be shown
                else:
                    messagebox.showwarning("Warning", "Please choose a destination file.")

            # Will catch exceptions if needed
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")

        # If the csv file path is not valid, will show a warning message box
        else:
            messagebox.showwarning("Warning", "Please choose a CSV file first")


    # Basically the instantiation function for the CSV_To_Excel_UI class
    # Creates the UI and displays it
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = tk.Toplevel()
        self.window.title("CSV -> Excel Converter")
        self.window.geometry("450x250")
        self.window.config(bg="gray")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Creates the main header label and places it via grid method
        headerLabel = Label(self.window, text='CSV -> Excel File Converter', font=('Arial', 18), fg='black', bg='white')
        headerLabel.grid(row=0, columnspan=2)

        # Creates a label for the csv entry box and places it via grid
        csvLabel = Label(self.window, text='CSV File:', font=('Arial', 12), fg='black', bg='white')
        csvLabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        # Creates the text entry box for the csv file to be entered and places it
        self.csvEntry = Entry(self.window, width=40)
        self.csvEntry.grid(row=1, column=1, padx=10, pady=5)

        # Creates a button that is attached to the choose_csv function
        # Lets a user select a file from their file system
        browseFilesBtn = Button(self.window, text="Browse", command=self.choose_csv)
        browseFilesBtn.grid(row=1, column=2, padx=10, pady=5)

        # Creates a button to call the file conversion function
        convertFileBtn = Button(self.window, text="Convert File", command=self.convert_csv_to_excel)
        convertFileBtn.grid(row=2, columnspan=3, padx=10, pady=5)

    # Shows the UI
    def show(self):
        self.window.mainloop()

    def on_close(self):
        self.window.destroy()
        self.main_window.deiconify()
