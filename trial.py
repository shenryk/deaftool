from tkinter import *
#import tkinter as tk
#from PIL import ImageTK
import pyttsx3


root = Tk ()
root.title('images')

engine = pyttsx3.init()
engine.say('hello world')
engine.runAndWait()

root.mainloop()
