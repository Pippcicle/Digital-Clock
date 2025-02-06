from tkinter import *
from tkinter.ttk import *

from time import strftime
import random 
 
root = Tk()
root.title ("Clock")

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)

color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
lbl = Label(root, font = ("ariel", 40, "bold"), background= color, foreground="#DEC1FF")
lbl.pack(anchor = CENTER)


def time():
    current_time = strftime("%H:%M:%S %p")
    lbl.config(text = current_time)
    lbl.after(1000, time)
    

time()

root.mainloop()