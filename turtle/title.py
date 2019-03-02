#GUI
import tkinter, turtle
from tkinter import *
root = tkinter.Tk()

#def workspace1
frame1 = Frame(root)
frame1.pack(side = LEFT)
frame1.geometry("100x150")

#def workspace2
frame2 = Frame(root)
frame2.pack(side = RIGHT)
#frame2.geometry("400x600")

def sel():
    selection = "Value = " + str(q.get())
    label.config(text = selection)

#Window settings
root.title("_______________OK")
root.geometry("800x600")
root.resizable(0,0)

q = DoubleVar()
scale = Scale(frame1, variable = q)
scale.pack(side = LEFT)


button = Button(frame1, text="Get Scale Value", command = sel)
button.pack(side = LEFT)


label = Label(frame2)
label.pack(side = BOTTOM)








#t = turtle.Turtle()
#circle = turtle.Turtle()
#for c in ['red', 'green', 'yellow', 'blue', 'pink', 'red', 'green', 'yellow', 'blue', 'pink']:
#    t.color(c)
#    t.forward(100)
#    t.left(100)
#    t.circle(120)
#circle.right(100)    
#circle.circle(50)


#root.resizable(width = false, height = false)
root.mainloop()

