import sys
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Piano")
root.geometry('900x300+0+0')
root.configure(background='white')

F=Frame(root, bg="white", bd=2)
F.grid()

C4=ttk.Button(F, width=6, text="C")
C4.grid(row=0, column=0, padx=0,pady=1, ipady=130, ipadx=0)

D4=ttk.Button(F, width=6, text="D")
D4.grid(row=0, column=1, padx=0,pady=1, ipady=130, ipadx=0)


root.resizable(width=0, height=0)
root.mainloop();


"""        noteList = ['A#1', 'A#2', 'A1', 'A2', 'B1', 'B2', 'C#1', 'C#2', 'C1', 'C2', 'D#1', 'D#2', \
                    'D1', 'D2', 'E1', 'E2', 'F#1', 'F#2', 'F1', 'F2', 'G#1', 'G#2', 'G1', 'G2']"""

