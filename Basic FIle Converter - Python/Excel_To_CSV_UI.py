# Imports tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
import pandas as pd

class Excel_To_CSV_UI:

    # Function that opens up a file dialog box and gets the user to select an excel file
    # If the file path is valid, it will change the excelEntry value accordingly
    def choose_excel(self):

        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])

        if file_path:
            self.excelEntry.delete(0, END)
            self.excelEntry.insert(0, file_path)

    # Function used to convert an excel file to a csv file
    # Takes the file selected by the user and uses pandas to convert it to a csv file
    def convert_excel_to_csv(self):

        # Gets the file path from the excelEntry box
        excel_file_path = self.excelEntry.get()

        # If the excel file path is valid then it will try to change it to a csv file where the user specifies the file path
        if excel_file_path:
            try:
                df = pd.read_excel(excel_file_path)

                csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                             filetypes=[("CSV files", "*.csv")])

                # If the csv file path chosen is valid, then the file will be converted, and it will show a messagebox
                if csv_file_path:
                    df.to_csv(excel_file_path, index=False)
                    messagebox.showinfo("Success",
                                        f"CSV file f'{excel_file_path}' has been successfully converted to Excel files '{csv_file_path}'")
                # Otherwise, a warning message box will be shown
                else:
                    messagebox.showwarning("Warning", "Please choose a destination file.")

            # Will catch exceptions if needed
            except Exception as e:
                messagebox.showwarning("Error", f"An error occurred: {str(e)}")

        # If the excel file path is not valid, will show a warning message box
        else:
            messagebox.showwarning("Warning", "Please choose an Excel file first")

    # Basically the instantiation function for the CSV_To_Excel_UI class
    # Creates the UI and displays it
    def __init__(self, main_window):
        self.main_window = main_window
        self.window = tk.Toplevel()
        self.window.title("Excel -> CSV Converter")
        self.window.geometry("450x250")
        self.window.config(bg="gray")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Creates the main header label and places it via grid method
        headerLabel = Label(self.window, text='Excel -> CSV File Converter', font=('Arial', 18), fg='black', bg='white')
        headerLabel.grid(row=0, columnspan=2)

        # Creates a label for the csv entry box and places it via grid
        excelLabel = Label(self.window, text='Excel File:', font=('Arial', 12), fg='black', bg='white')
        excelLabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        # Creates the text entry box for the csv file to be entered and places it
        self.excelEntry = Entry(self.window, width=40)
        self.excelEntry.grid(row=1, column=1, padx=10, pady=5)

        # Creates a button that is attached to the choose_csv function
        # Lets a user select a file from their file system
        browseFilesBtn = Button(self.window, text="Browse", command=self.choose_excel)
        browseFilesBtn.grid(row=1, column=2, padx=10, pady=5)

        # Creates a button to call the file conversion function
        convertFileBtn = Button(self.window, text="Convert File", command=self.convert_excel_to_csv)
        convertFileBtn.grid(row=2, columnspan=3, padx=10, pady=5)

    # Shows the UI
    def show(self):
        self.window.mainloop()

    def on_close(self):
        self.window.destroy()
        self.main_window.deiconify()
