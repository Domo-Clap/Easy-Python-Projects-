# Imports tkinter
import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox

from pdf2docx import parse
from typing import Tuple


class PDF_To_Docx_UI:

    # Function that opens up a file dialog box and gets the user to select a csv file
    # If the file path is valid, it will change the csvEntry value accordingly
    def choose_PDF(self):

        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if file_path:
            self.pdfEntry.delete(0, END)
            self.pdfEntry.insert(0, file_path)


    def convert_pdf_to_docx(self):

        input_file = self.pdfEntry.get()

        if not input_file:
            messagebox.showerror("Error", "Please select a PDF file")
            return

        output_file = filedialog.asksaveasfilename(defaultextension=".docx",
                                                   filetypes=[("Word Document", "*.docx")])

        if not output_file:
            return

        result = parse(pdf_file=input_file, docx_with_path=output_file)
        messagebox.showinfo("Success", "Conversion completed successfully.")


    def __init__(self, main_window):
        self.main_window = main_window
        self.window = tk.Toplevel()
        self.window.title("PDF -> Docx Converter")
        self.window.geometry("450x250")
        self.window.config(bg="gray")
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

        # Creates the main header label and places it via grid method
        headerLabel = Label(self.window, text='PDF -> Docx File Converter', font=('Arial', 18), fg='black', bg='white')
        headerLabel.grid(row=0, columnspan=2)

        # Creates a label for the csv entry box and places it via grid
        pdfLabel = Label(self.window, text='PDF File:', font=('Arial', 12), fg='black', bg='white')
        pdfLabel.grid(row=1, column=0, padx=10, pady=5, sticky="e")

        # Creates the text entry box for the csv file to be entered and places it
        self.pdfEntry = Entry(self.window, width=40)
        self.pdfEntry.grid(row=1, column=1, padx=10, pady=5)

        # Creates a button that is attached to the choose_csv function
        # Lets a user select a file from their file system
        browseFilesBtn = Button(self.window, text="Browse", command=self.choose_PDF)
        browseFilesBtn.grid(row=1, column=2, padx=10, pady=5)

        # Creates a button to call the file conversion function
        convertFileBtn = Button(self.window, text="Convert File", command=self.convert_pdf_to_docx)
        convertFileBtn.grid(row=2, columnspan=3, padx=10, pady=5)

    # Shows the UI
    def show(self):
        self.window.mainloop()

    def on_close(self):
        self.window.destroy()
        self.main_window.deiconify()
