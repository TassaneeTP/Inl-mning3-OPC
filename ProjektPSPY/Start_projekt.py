
import random 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os
import subprocess

root = Tk()
root.geometry('905x700')
root.title('Hangman Game')
root.config(bg = '#FFEFDB')

Play = Button(root, text="PLay(Bot)", fg="blue", bg="cyan", 
              command=lambda:subprocess.Popen(args=['python', r'C:\Users\tas_m\source\repos\ProjektPSPY\ProjektPSPY']))

