from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.geometry("300x400")

text = ""

top = Frame(root)
bottom = Frame(root)

txtarea = Label(top, width=15, text=text, font=("Arial", 20), bg="lightgrey")
txtarea.pack()

def button_1_click():
    global text
    text += "1"
    txtarea.config(text=text)

def button_2_click():
    global text
    text += "2"
    txtarea.config(text=text)

def button_3_click():
    global text
    text += "3"
    txtarea.config(text=text)

def button_4_click():
    global text
    text += "4"
    txtarea.config(text=text)

def button_5_click():
    global text
    text += "5"
    txtarea.config(text=text)

def button_6_click():
    global text
    text += "6"
    txtarea.config(text=text)

def button_7_click():
    global text
    text += "7"
    txtarea.config(text=text)

def button_8_click():
    global text
    text += "8"
    txtarea.config(text=text)

def button_9_click():
    global text
    text += "9"
    txtarea.config(text=text)

def button_0_click():
    global text
    text += "0"
    txtarea.config(text=text)


btn1 = Button(bottom, text="1", font=("Arial", 20), command=button_1_click)
btn2 = Button(bottom, text="2", font=("Arial", 20), command=button_2_click)
btn3 = Button(bottom, text="3", font=("Arial", 20), command=button_3_click)    
btn4 = Button(bottom, text="4", font=("Arial", 20), command=button_4_click)
btn5 = Button(bottom, text="5", font=("Arial", 20), command=button_5_click)
btn6 = Button(bottom, text="6", font=("Arial", 20), command=button_6_click)
btn7 = Button(bottom, text="7", font=("Arial", 20), command=button_7_click)
btn8 = Button(bottom, text="8", font=("Arial", 20), command=button_8_click)
btn9 = Button(bottom, text="9", font=("Arial", 20), command=button_9_click)
btn0 = Button(bottom, text="0", font=("Arial", 20), command=button_0_click)

btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn7.grid(column=0, row=3)
btn8.grid(column=1, row=3)
btn9.grid(column=2, row=3)
btn0.grid(column=0, row=4)

top.pack()
bottom.pack()

root.mainloop()