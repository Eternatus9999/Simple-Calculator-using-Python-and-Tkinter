from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.geometry("300x400")

text = ""

top = Frame(root)
bottom = Frame(root)

textarea = Label(top, width=15, text=text, font=("Arial", 20), bg="lightgrey")
textarea.pack()

def button_1_click():
    global text
    text += "1"
    textarea.config(text=text)

def button_2_click():
    global text
    text += "2"
    textarea.config(text=text)

def button_3_click():
    global text
    text += "3"
    textarea.config(text=text)

def button_4_click():
    global text
    text += "4"
    textarea.config(text=text)

def button_5_click():
    global text
    text += "5"
    textarea.config(text=text)

def button_6_click():
    global text
    text += "6"
    textarea.config(text=text)

def button_7_click():
    global text
    text += "7"
    textarea.config(text=text)

def button_8_click():
    global text
    text += "8"
    textarea.config(text=text)

def button_9_click():
    global text
    text += "9"
    textarea.config(text=text)

def button_0_click():
    global text
    text += "0"
    textarea.config(text=text)

def button_point_click():
    global text
    text += "."
    textarea.config(text=text)

def button_addition():
    global text
    text += " + "
    textarea.config(text=text)

def button_subtract():
    global text
    text += " - "
    textarea.config(text=text)

def button_multiply():
    global text
    text += " * "
    textarea.config(text=text)

def button_divide():
    global text
    text += " / "
    textarea.config(text=text)

def button_equal():
    global text
    text = str(eval(text))
    textarea.config(text=text)


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
btn_point = Button(bottom, text=".", font=("Arial", 20), command=button_point_click)
btn_add = Button(bottom, text="+", font=("Arial", 20), command=button_addition)
btn_sub = Button(bottom, text="-", font=("Arial", 20), command=button_subtract)
btn_mul = Button(bottom, text="*", font=("Arial", 20), command=button_multiply)
btn_div = Button(bottom, text="/", font=("Arial", 20), command=button_divide)
btn_equ = Button(bottom, text="=", font=("Arial", 20), command=button_equal)

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
btn_point.grid(column=1, row=4)
btn_add.grid(column=3, row=1)
btn_sub.grid(column=3, row=2)
btn_mul.grid(column=3, row=3)
btn_div.grid(column=3, row=4)
btn_equ.grid(column=2, row=4)

top.pack()
bottom.pack()

root.mainloop()