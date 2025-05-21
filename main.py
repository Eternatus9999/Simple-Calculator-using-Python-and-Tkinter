from tkinter import *

root = Tk()

root.title("Simple Calculator")
root.geometry("265x300")

root.configure(bg="lightgrey")

text = ""

top = Frame(root)
bottom = Frame(root)

bottom.configure(bg="lightgrey")

textarea = Label(top, width=15, text=text, font=("Arial", 20))
textarea.pack()

# Functions of the buttons

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
    text += "+"
    textarea.config(text=text)

def button_subtract():
    global text
    text += "-"
    textarea.config(text=text)

def button_multiply():
    global text
    text += "*"
    textarea.config(text=text)

def button_divide():
    global text
    text += "/"
    textarea.config(text=text)

def button_equal():
    global text
    text = str(eval(text))
    textarea.config(text=text)

def button_clear():
    global text
    text = ""
    textarea.config(text=text)

def button_delete():
    global text
    text = text[:-1]
    textarea.config(text=text)

def button_open_bracket():
    global text
    text += "("
    textarea.config(text=text)

def button_close_bracket():
    global text
    text += ")"
    textarea.config(text=text)


# GUI Buttons

btn1 = Button(bottom, text="1", font=("Arial", 20), command=button_1_click, activebackground="grey", activeforeground="white", width=3)
btn2 = Button(bottom, text="2", font=("Arial", 20), command=button_2_click, activebackground="grey", activeforeground="white", width=3)
btn3 = Button(bottom, text="3", font=("Arial", 20), command=button_3_click, activebackground="grey", activeforeground="white", width=3)    
btn4 = Button(bottom, text="4", font=("Arial", 20), command=button_4_click, activebackground="grey", activeforeground="white", width=3)
btn5 = Button(bottom, text="5", font=("Arial", 20), command=button_5_click, activebackground="grey", activeforeground="white", width=3)
btn6 = Button(bottom, text="6", font=("Arial", 20), command=button_6_click, activebackground="grey", activeforeground="white", width=3)
btn7 = Button(bottom, text="7", font=("Arial", 20), command=button_7_click, activebackground="grey", activeforeground="white", width=3)
btn8 = Button(bottom, text="8", font=("Arial", 20), command=button_8_click, activebackground="grey", activeforeground="white", width=3)
btn9 = Button(bottom, text="9", font=("Arial", 20), command=button_9_click, activebackground="grey", activeforeground="white", width=3)
btn0 = Button(bottom, text="0", font=("Arial", 20), command=button_0_click, activebackground="grey", activeforeground="white", width=3)
btn_point = Button(bottom, text=".", font=("Arial", 20), command=button_point_click, activebackground="grey", activeforeground="white", width=2)
btn_add = Button(bottom, text="+", font=("Arial", 20), command=button_addition, activebackground="grey", activeforeground="white", width=2)
btn_sub = Button(bottom, text="-", font=("Arial", 20), command=button_subtract, activebackground="grey", activeforeground="white", width=2)
btn_mul = Button(bottom, text="*", font=("Arial", 20), command=button_multiply, activebackground="grey", activeforeground="white", width=2)
btn_div = Button(bottom, text="/", font=("Arial", 20), command=button_divide, activebackground="grey", activeforeground="white", width=2)
btn_delete = Button(bottom, text="del", font=("Arial", 16), command=button_delete, activebackground="grey", activeforeground="white", width=3, height=1)
btn_open_bracket = Button(bottom, text="(", font=("Arial",20),command=button_open_bracket, activebackground="grey", activeforeground="white", width=3)
btn_close_bracket = Button(bottom, text=")", font=("Arial",20),command=button_close_bracket, activebackground="grey", activeforeground="white", width=3)
btn_equ = Button(bottom, text="=", font=("Arial", 20), bg="green", command=button_equal)
btn_clear = Button(bottom, text="C", font=("Arial", 20), bg="red", command=button_clear)

# Button Layout

# row1

btn1.grid(column=0, row=1)
btn2.grid(column=1, row=1)
btn3.grid(column=2, row=1)
btn_add.grid(column=3, row=1)
btn_clear.grid(column=4, row=1)

# row2

btn4.grid(column=0, row=2)
btn5.grid(column=1, row=2)
btn6.grid(column=2, row=2)
btn_sub.grid(column=3, row=2)
btn_delete.grid(column=4, row=2)

# row3

btn7.grid(column=0, row=3)
btn8.grid(column=1, row=3)
btn9.grid(column=2, row=3)
btn_div.grid(column=3, row=3)
btn_mul.grid(column=4, row=3)

# row4

btn_open_bracket.grid(column=0, row=4)
btn0.grid(column=1, row=4)
btn_close_bracket.grid(column=2, row=4)
btn_point.grid(column=3, row=4)
btn_equ.grid(column=4, row=4)

top.pack()
bottom.pack()

root.mainloop()