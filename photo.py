from tkinter import *

#from PIL import Image, ImageTk
from PIL import Image

root = Tk()

photo = PhotoImage(file = 'kingel-words.png')
#label = Label(root, image = photo)
#label.pack()

label_kingel = Label(root,text = "Thank you for buying kingel ")

def kingel_click():
    return label_kingel





kingel_button = Button(root,image=photo,pady=20,padx=20,command=kingel_click)
kingel_button.pack()
root.mainloop()
