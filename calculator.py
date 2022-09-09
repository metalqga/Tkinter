import tkinter
from tkinter import *
from math import *

# global vars
sign = None
list_num = []
memory = 0

root = Tk()
root.title("A simple Python Calculator using Tkinter")


def button_click(number):
    value = e.get()
    if value == "0" and number != ".":
        e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def ce():
    global list_num
    list_num = []
    e.delete(0, END)


def c():
    # del list_num[1]
    e.delete(0, END)


def plusminus():
    value = float(e.get())
    try:
        value / int(value)
        if value / int(value) == 1:
            value = int(e.get())
        e.delete(0, END)
        e.insert(0, (-value))
    except:
        e.delete(0, END)
        e.insert(0, (-value))


def percentage():
    value = float(e.get()) * float(list_num[0]) / 100
    e.delete(0, END)
    e.insert(0, (value))


def sqrt1():
    value = sqrt(float(e.get()))
    e.delete(0, END)
    e.insert(0, value)


def memoryplus():
    try:
        value = float(e.get())
    except ValueError:
        return
    value = float(e.get())
    if value / int(value) == 1:
        value = int(value)
    global memory
    memory += value
    # add memory icon
    if memory != 0:
        button_memory.grid(row=0, column=0)
    e.delete(0, END)
    e.insert(0, "0")


def memoryminus():
    try:
        value = float(e.get())
    except ValueError:
        return
    value = float(e.get())
    if value / int(value) == 1:
        value = int(value)
    global memory
    memory -= value
    # add memory icon
    if memory != 0:
        button_memory.grid(row=0, column=0)
    e.delete(0, END)
    e.insert(0, "0")


def rclmem():
    global memory
    if e.get()!="":
        value = float(e.get())
        if value == memory:
            memory = 0
            # remove memory icon
            button_memory.grid_forget()

    e.delete(0, END)
    e.insert(0, memory)


def add():
    global sign
    sign = "+"
    first_num = e.get()
    list_num.insert(0, first_num)
    e.delete(0, END)


def sub():
    global sign
    sign = "-"
    first_num = e.get()
    list_num.insert(0, first_num)
    e.delete(0, END)


def mul():
    global sign
    sign = "*"
    first_num = e.get()
    list_num.insert(0, first_num)
    e.delete(0, END)


def div():
    global sign
    sign = "/"
    first_num = e.get()
    list_num.insert(0, first_num)
    e.delete(0, END)


def equal(sign):
    #if no number, just continue
    if e.get() == "":
        return
    # get last number
    list_num.insert(0, e.get())

    # clear screen
    e.delete(0, END)

    # do the calculations
    if sign == "+":
        result = (float(list_num[1]) + float(list_num[0]))
        if result / int(result) == 1:
            result = int(result)

    elif sign == "-":
        result = (float(list_num[1]) - float(list_num[0]))
        if result == 0:
            e.insert(0, "0")
            return
        if result / int(result) == 1:
            result = int(result)

    elif sign == "/":
        if list_num[0] == "0":
            e.insert(0, ("0 division! Try again."))
        else:
            result = (float(list_num[1]) / float(list_num[0]))
            if result / int(result) == 1:
                result = int(result)

    elif sign == "*":
        result = (float(list_num[0]) * float(list_num[1]))
        if result / int(result) == 1:
            result = int(result)

    e.insert(0, round(result,8))

# screen
e = Entry(root, background="#d3d3d3", font=('Times', '48', 'bold'), width=10, borderwidth=10, justify=tkinter.RIGHT)
e.grid(row=0, column=0, columnspan=10, padx=10, pady=20)
e.insert(0, "0")

# Define Buttons
button_1 = Button(root, text="1", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                  command=lambda: button_click(0))

# + - * / . =  clr
button_plus = Button(root, text="+", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20, command=add)
button_minus = Button(root, text="-", font=('Times', '24', 'bold'), borderwidth=5, padx=23, pady=20, command=sub)
button_mul = Button(root, text="*", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20, command=mul)
button_div = Button(root, text="/", font=('Times', '24', 'bold'), borderwidth=5, padx=23, pady=20, command=div)
button_decimal = Button(root, text=".", font=('Times', '24', 'bold'), borderwidth=5, padx=23, pady=20,
                        command=lambda: button_click("."))
button_equal = Button(root, text="=", font=('Times', '24', 'bold'), borderwidth=5, padx=20, pady=20,
                      command=lambda: equal(sign))
# button_clear = Button(root, text = "CLR", font=('Times', '18', 'bold'), borderwidth=5, padx=5, pady=5, command=clear)

# sqrt, mrc, m- m+ % +/- C AC
button_c = Button(root, text="C", font=('Times', '24', 'bold'), borderwidth=5, padx=22, pady=20, command=c)
button_ac = Button(root, text="AC", font=('Times', '24', 'bold'), borderwidth=5, padx=12, pady=20, command=ce)
button_sqrt = Button(root, text="√", font=('Times', '24'), borderwidth=5, padx=26, pady=8, command=sqrt1)
button_percent = Button(root, text="%", font=('Times', '24', 'bold'), borderwidth=5, padx=18, pady=18,
                        command=percentage)
button_mrc = Button(root, text="MC", font=('Times', '24', 'bold'), borderwidth=5, padx=0, pady=8, command=rclmem)
button_mm = Button(root, text="M-", font=('Times', '24', 'bold'), borderwidth=5, padx=10, pady=8, command=memoryminus)
button_mp = Button(root, text="M+", font=('Times', '24', 'bold'), borderwidth=5, padx=4, pady=8, command=memoryplus)
button_plusminus = Button(root, text="+/-", font=('Times', '24', 'bold'), borderwidth=5, padx=14, pady=20,
                          command=plusminus)
# memory indicator
button_memory = Button(root, text="M", font=('Times', '10', 'bold'), background="white", state=DISABLED)

# Put buttons on screen
button_1.grid(row=4, column=1)
button_2.grid(row=4, column=2)
button_3.grid(row=4, column=3)
button_4.grid(row=3, column=1)
button_5.grid(row=3, column=2)
button_6.grid(row=3, column=3)
button_7.grid(row=2, column=1)
button_8.grid(row=2, column=2)
button_9.grid(row=2, column=3)
button_0.grid(row=5, column=1)

button_decimal.grid(row=5, column=2)
button_plus.grid(row=5, column=5)
button_minus.grid(row=4, column=5)
button_mul.grid(row=3, column=5)
button_div.grid(row=2, column=5)
button_equal.grid(row=5, column=3)

button_sqrt.grid(row=1, column=0)
button_percent.grid(row=2, column=0)
button_plusminus.grid(row=3, column=0)
button_c.grid(row=4, column=0)
button_ac.grid(row=5, column=0)

button_mrc.grid(row=1, column=1)
button_mm.grid(row=1, column=2)
button_mp.grid(row=1, column=3)

root.mainloop()
