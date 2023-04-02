import tkinter as tk
import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        os.system('notepad "{}"'.format(file_path))

window = tk.Tk()
window.title("CH File opener")
window.geometry("300x300")

hello = tk.Label(text="Welcome to the CH file opener! Click Find \n to open a file and edit it! \n Currently, this program can only open text \n documents and not code. ")
hello.pack()
button = tk.Button(window, text="Find", command=open_file)
button.pack()

tk.mainloop()