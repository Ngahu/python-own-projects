from tkinter import *
from tkFileDialog import *

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    
def saveFile():
    global filename
    t = text.get(0.0, END)