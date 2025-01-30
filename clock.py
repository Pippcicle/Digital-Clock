#importing the libraries
from tkinter import *
from tkinter.ttk import *

from time import strftime 

#creating the GUI elements 
root = Tk()
root.title ("Clock")

lbl = Label(root, font = ("ariel", 40, "bold"), background= "#7D70BA", foreground = "#DEC1FF")
lbl.pack(anchor = CENTER)

def time():
    current_time = strftime("%H:%M:%S %p")
    lbl.config(text = current_time)
    lbl.after(1000, time)

time()











root.mainloop()