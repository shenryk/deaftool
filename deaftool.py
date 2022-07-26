from tkinter import *
import pyttsx3
from tkinter import ttk

root = Tk()
root.title("Sign Language Teacher & Helper")
root.geometry("500x500")
root.resizable(True,True)

#scrollbar
#create a main frame
main_frame = Frame(root)
main_frame.pack(fill = BOTH, expand = 1)
#create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH, expand=1)
#add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
my_scrollbar.pack(side= RIGHT,fill=Y)
#configure the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))
#add anothe FRAME inside the canvas
second_frame = Frame(my_canvas)
#add that new frame to a window inside the CANVAS
my_canvas.create_window((0,0),window = second_frame, anchor = "nw")

my_entry= Entry(second_frame,width=35,borderwidth=3)
my_entry.grid(row=0,columnspan=6,padx=10,pady=10)


#do nothing
def doNothing():
    print('wont do are thing')
    #label_1=Label(root,text='doing nothing').pack()
#expressions
def home():
	engine = pyttsx3.init()
	engine.say("home")
	engine.runAndWait()

#def talk():
    #engine = pyttsx3.init()
	#engine.say(my_entry.get())
	#engine.runAndWait()
	

def speak():
	engine = pyttsx3.init()
	engine.say(my_entry.get())
	engine.runAndWait()
	my_entry.delete(0,END)

def you():
	engine = pyttsx3.init()
	engine.say("you")
	engine.runAndWait()

def happy():
	engine = pyttsx3.init()
	engine.say("happy")
	engine.runAndWait()

def car():
	engine = pyttsx3.init()
	engine.say("car")
	engine.runAndWait()

#Alphabet
def button_click(string):
    current = my_entry.get()
    my_entry.delete(0,END)
    my_entry.insert(0,str(current)+str(string))



sign_a = PhotoImage (file = 'a.png')
sign_b = PhotoImage (file = 'b.png')
sign_c = PhotoImage (file = 'c.png')
sign_d = PhotoImage (file = 'd.png')
sign_e = PhotoImage (file = 'e.png')

sign_f = PhotoImage (file = 'f.png')
sign_g = PhotoImage (file = 'g.png')
sign_h = PhotoImage (file = 'h.png')
sign_i = PhotoImage (file = 'i.png')
sign_j = PhotoImage (file = 'j.png')

sign_k = PhotoImage (file = 'k.png')
sign_l = PhotoImage (file = 'l.png')
sign_m = PhotoImage (file = 'm.png')
sign_n = PhotoImage (file = 'n.png')
sign_o = PhotoImage (file = 'o.png')

sign_p = PhotoImage (file = 'p.png')
sign_q = PhotoImage (file = 'q.png')
sign_r = PhotoImage (file = 'r.png')
sign_s = PhotoImage (file = 's.png')
sign_t = PhotoImage (file = 't.png')

sign_u = PhotoImage (file = 'u.png')
sign_v = PhotoImage (file = 'v.png')
sign_w = PhotoImage (file = 'w.png')
sign_x = PhotoImage (file = 'x.png')
sign_y = PhotoImage (file = 'y.png')

sign_z = PhotoImage (file = 'z.png')


#adding some buttons
button_1=Button(second_frame,image = sign_a,padx=20,pady=10,borderwidth=0, command=lambda: button_click('a'))
button_2=Button(second_frame,image =sign_b,padx=20,pady=20,borderwidth=0,command=lambda: button_click('b'))
button_3=Button(second_frame,image =sign_c,padx=20,pady=20,borderwidth=0,command=lambda: button_click('c'))
button_4=Button(second_frame,image =sign_d,padx=20,pady=20,borderwidth=0,command=lambda: button_click('d'))
button_5=Button(second_frame,image =sign_e,padx=20,pady=20,borderwidth=0,command=lambda: button_click('e'))

button_6=Button(second_frame,image =sign_f,padx=20,pady=20,borderwidth=0,command=lambda: button_click('f'))
button_7=Button(second_frame,image =sign_g,padx=20,pady=20,borderwidth=0,command=lambda: button_click('g'))
button_8=Button(second_frame,image =sign_h,padx=20,pady=20,borderwidth=0,command=lambda: button_click('h'))
button_9=Button(second_frame,image =sign_i,padx=20,pady=20,borderwidth=0,command=lambda: button_click('i'))
button_10=Button(second_frame,image =sign_j,padx=20,pady=20,borderwidth=0,command=lambda: button_click('j'))

button_11=Button(second_frame,image =sign_k,padx=20,pady=20,borderwidth=0,command=lambda: button_click('k'))
button_12=Button(second_frame,image =sign_l,padx=20,pady=20,borderwidth=0,command=lambda: button_click('l'))
button_13=Button(second_frame,image =sign_m,padx=20,pady=20,borderwidth=0,command=lambda: button_click('m'))
button_14=Button(second_frame,image =sign_n,padx=20,pady=20,borderwidth=0,command=lambda: button_click('n'))
button_15=Button(second_frame,image =sign_o,padx=20,pady=20,borderwidth=0,command=lambda: button_click('o'))

button_16=Button(second_frame,image =sign_p,padx=20,pady=20,borderwidth=0,command=lambda: button_click('p'))
button_17=Button(second_frame,image =sign_q,padx=20,pady=20,borderwidth=0,command=lambda: button_click('q'))
button_18=Button(second_frame,image =sign_r,padx=20,pady=20,borderwidth=0,command=lambda: button_click('r'))
button_19=Button(second_frame,image =sign_s,padx=20,pady=20,borderwidth=0,command=lambda: button_click('s'))
button_20=Button(second_frame,image =sign_t,padx=20,pady=20,borderwidth=0,command=lambda: button_click('t'))

button_21=Button(second_frame,image =sign_u,padx=20,pady=20,borderwidth=0,command=lambda: button_click('u'))
button_22=Button(second_frame,image =sign_v,padx=20,pady=20,borderwidth=0,command=lambda: button_click('v'))
button_23=Button(second_frame,image =sign_w,padx=20,pady=20,borderwidth=0,command=lambda: button_click('w'))
button_24=Button(second_frame,image =sign_x,padx=20,pady=20,borderwidth=0,command=lambda: button_click('x'))
button_25=Button(second_frame,image =sign_y,padx=20,pady=20,borderwidth=0,command=lambda: button_click('y'))

button_26=Button(second_frame,image =sign_z,padx=20,pady=20,borderwidth=0,command=lambda: button_click('z'))
button_talk = Button(second_frame ,text='speak',padx=20,pady=20,borderwidth=4, command = speak)
#button_add=Button(root,image =sign_f,padx=39,pady=20,command=button_add)
#button_equal=Button(root,image =sign_f,padx=91,pady=20,command=button_equal)
#button_clear=Button(root,image =sign_fclea=sign_f,padx=79,pady=20,command=button_clear)

#button_subtract=Button(root,image =sign_f,padx=41,pady=20,command=button_subtract)
#button_multiply=Button(root,image =sign_f,padx=20,pady=20,command=button_multiply)
#button_divide=Button(root,image =sign_f,padx=20,pady=20,command=button_divide)

#putting buttons onto the screen
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=1,column=3)
button_5.grid(row=1,column=4)


button_6.grid(row=2,column=0)
button_7.grid(row=2,column=1)
button_8.grid(row=2,column=2)
button_9.grid(row=2,column=3)
button_10.grid(row=2,column=4)

button_11.grid(row=3,column=0)
button_12.grid(row=3,column=1)
button_13.grid(row=3,column=2)
button_14.grid(row=3,column=3)
button_15.grid(row=3,column=4)

button_16.grid(row=4,column=0)
button_17.grid(row=4,column=1)
button_18.grid(row=4,column=2)
button_19.grid(row=4,column=3)
button_20.grid(row=4,column=4)

button_21.grid(row=5,column=0)
button_22.grid(row=5,column=1)
button_23.grid(row=5,column=2)
button_24.grid(row=5,column=3)
button_25.grid(row=5,column=4)

button_26.grid(row=6,column=0)
button_talk.grid(row=2, column=5)
#button_clear.grid(row=4,column=1,columnspan=2)
#button_add.grid(row=5,column=0)
#button_equal.grid(row=5,column=1,columnspan=2)

#button_subtract.grid(row=6,column=0)
#button_multiply.grid(row=6,column=1)
#button_divide.grid(row=6,column=2)

#menus
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="More",menu=subMenu)
subMenu.add_command(label='Expressions',command=doNothing)
subMenu.add_command(label='More signs',command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit',command=quit)

editMenu =Menu(menu)
menu.add_cascade(label='save',menu=editMenu)
editMenu.add_command(label='about',command=doNothing)




root.mainloop()
