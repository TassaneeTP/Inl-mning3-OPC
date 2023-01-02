from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ProjektPSPY

root = Tk()
root.geometry('905x700')
root.title('Hangman Game')
root.config(bg = '#FFEFDB')

Label(root, text= "Click the below button to Start the game", font= ('Helvetica 17 bold')).pack(pady=30)
B = ttk.Button(root, text = "Start", command = ProjektPSPY).pack(pady=10)
root.mainloop()



