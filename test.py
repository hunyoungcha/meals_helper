import tkinter as tk
from tkinter import filedialog

def Load():
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("PPTX files", "*.pptx"),
                                          ("all files", "*.*")))
    print(filename)

Load