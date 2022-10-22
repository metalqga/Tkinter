
from py_expression_eval import Parser
from buttons import *
# from main import e, result_screen, equations_memory
from math import *
import random
from body import *
from fractions import Fraction
# global vars
# default will be in degrees
memory = 0
mode_state = 1

# cursor beginning coordinates
x = 1.0
y = 60.0
eq_no = 0
equations_memory = []


def expression_parser(a=""):
    parser = Parser()
    original_expression = e.get(index1=1.0, index2=END).strip()
    equations_memory.append(original_expression)
    result = parser.parse(original_expression).evaluate({})
    # result = parser.evaluate(original_expression, {})
    print(result)
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(index=1.0, chars=str(result))
    # align the result to the right
    result_screen.tag_configure("right", justify='right')
    result_screen.tag_add("right", 1.0, "end")


def button_click(number):
    value = e.get(index1=1.0, index2=END)
    if value == "0" and number != ".":
        e.delete(index1=1.0, index2=END)
    current = e.get(END)
    # e.delete(index1=1.0, index2=END)
    e.insert(END, str(current) + str(number))


def ce():
    global list_num
    # list_num = []
    e.delete(index1=1.0, index2=END)
    result_screen.delete(index1=1.0, index2=END)


def memoryplus():
    try:
        value = float(result_screen.get(index1=1.0, index2=END))
    except ValueError:
        return
    value = float(result_screen.get(index1=1.0, index2=END))
    if value >= 1:
        if value / int(value) == 1:
            value = int(value)
    global memory
    memory += value
    # add memory icon
    if memory != 0:
        button_memory.grid(row=0, column=0, sticky=NW)
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, "0")
    result_screen.tag_configure("right", justify='right')
    result_screen.tag_add("right", 1.0, "end")


def memoryminus():
    try:
        value = float(result_screen.get(index1=1.0, index2=END))
    except ValueError:
        return
    value = float(result_screen.get(index1=1.0, index2=END))
    if value / int(value) == 1:
        value = int(value)
    global memory
    memory -= value
    # add memory icon
    if memory != 0:
        button_memory.grid(row=0, column=0)
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, "0")
    result_screen.tag_configure("right", justify='right')
    result_screen.tag_add("right", 1.0, "end")


def rclmem():
    global memory
    screen_showing = result_screen.get(index1=1.0, index2=END)
    if screen_showing != "":

        value = float(screen_showing)
        if value == memory:
            memory = 0
            # remove memory icon
            button_memory.grid_forget()

    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, str(memory))
    result_screen.tag_configure("right", justify='right')
    result_screen.tag_add("right", 1.0, "end")


def x1():
    e.insert(END, "TODO")
    print(equations_memory)




def randomnum():
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, f"{random.random():.3f}")


# TODO
# bind cursor psn to DEL button
# update y as per entry screen len()
def end_cursor():
    global x, y
    screen_showing = e.get(index1=1.0, index2=END)
    y = len(screen_showing) - 1
    e.mark_set("insert", "%d.%d" % (x, y))


def zero_cursor():
    global x, y
    y = 0
    e.mark_set("insert", "%d.%d" % (x, y))


def move_cursor(arrow):
    global x, y
    if arrow == "◄":
        y -= 1.0
    else:
        y += 1.0
    e.mark_set("insert", "%d.%d" % (x, y))


def delete():
    global x, y
    displaying = e.get(index1=1.0, index2=END)
    if y == 60:
        e.delete(index1=1.0, index2=END)
        e.insert(END, displaying[:-2])
    else:
        e.delete(index1=1.0, index2=END)
        e.insert(END, displaying[:int(y - 1)] + displaying[int(y):].strip())
        y -= 1
        if y <= 0:
            screen_showing = e.get(index1=1.0, index2=END)
            y = len(screen_showing) - 1


def ans():
    displaying = result_screen.get(index1=1.0, index2=END).strip()
    e.delete(index1=1.0, index2=END)
    e.insert(END, displaying)


# use math.log10(num) to find out the x10 then check the number before that
def eng():
    displaying = float((result_screen.get(index1=1.0, index2=END).strip()))
    power10 = floor(log10(displaying))
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, str(displaying / pow(10, (power10))) + "x10" + get_super(str(power10)))


# function to convert to superscript
def get_super(digit):
    normal_digits = "0123456789+-"
    super_digits = "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻"
    result = digit.maketrans(''.join(normal_digits), ''.join(super_digits))
    return digit.translate(result)


# rad degr
def mode():
    global mode_state
    global button_sin
    global button_cos
    global button_tan
    global button_sin1
    global button_cos1
    global button_tan1
    mode_state += 1

    if mode_state % 2 == 0:
        radian = True
        button_radians.place(x=290, y=350)
        button_sin = Button(root, text="sin", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("sin("))
        button_cos = Button(root, text="cos", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("cos("))
        button_tan = Button(root, text="tan", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("tan("))
        button_sin1 = Button(root, text="asin", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("asin("))
        button_cos1 = Button(root, text="acos", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("acos("))
        button_tan1 = Button(root, text="atan", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("atan("))

    else:
        radian = False
        button_sin.place_forget()
        button_cos.place_forget()
        button_tan.place_forget()
        button_sin1.place_forget()
        button_cos1.place_forget()
        button_tan1.place_forget()
        button_radians.place_forget()
        button_sin = Button(root, text="sin", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("sind("))
        button_cos = Button(root, text="cos", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("cosd("))
        button_tan = Button(root, text="tan", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                            command=lambda: button_click("tand("))
        button_sin1 = Button(root, text="asin", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("asind("))
        button_cos1 = Button(root, text="acos", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("acosd("))
        button_tan1 = Button(root, text="atan", font=('Times', '12', 'bold'), width=5, borderwidth=1,
                             command=lambda: button_click("atand("))

    button_sin.place(x=172, y=280)
    button_cos.place(x=230, y=280)
    button_tan.place(x=290, y=280)


# start with 0 on screen
# e.insert(END, "0")

def eq_memory(step):
    global eq_no
    e.delete(index1=1.0, index2=END)
    e.insert(END, str(equations_memory[-1 - eq_no]))
    eq_no += step
    if eq_no == len(equations_memory):
        eq_no = 0
    elif eq_no < 0:
        eq_no = len(equations_memory) - 1


def on():
    result_screen.delete(index1=1.0, index2=END)
    result_screen.insert(END, "0")
    result_screen.tag_configure("right", justify='right')
    result_screen.tag_add("right", 1.0, "end")


def cd():
    number = (result_screen.get(index1=1.0, index2=END))
    fraction = Fraction(number).limit_denominator(10000000000)
    if True:
        result_screen.delete(index1=1.0, index2=END)
        result_screen.insert(END, f"{fraction}")
        result_screen.tag_configure("right", justify='right')
        result_screen.tag_add("right", 1.0, "end")


def to_degrees():
    # to degrees and back to float
    on_screen_result = (result_screen.get(index1=1.0, index2=END))
    try:
        float(on_screen_result)
        num = float(result_screen.get(index1=1.0, index2=END))
        decimals = num - int(num)
        degs = num - decimals
        mins = decimals * 60
        decimin = (mins - int(mins))
        seconds = decimin * 60
        result = (f"{int(degs)}º{int(mins)}\'{seconds:.0f}")
        result_screen.delete(index1=1.0, index2=END)
        result_screen.insert(END, f"{result}")
        result_screen.tag_configure("right", justify='right')
        result_screen.tag_add("right", 1.0, "end")
    except ValueError:
        degr = result_screen.get(index1=1.0, index2=END).strip()
        if degr == "":
            button_click("º")
        else:
            whole_num = ""
            mins = ""
            whole_mins = ""
            seconds = ""
            if len(degr) >= 5:
                for i in range(len(degr)):
                    if degr[i] != "º":
                        whole_num += degr[i]
                    else:
                        mins = degr[(i + 1):]
                        break
                for j in range(len(mins)):
                    if mins[j] != "'":
                        whole_mins += mins[j]
                    else:
                        seconds = mins[(j + 1):]
                        break
                seconds = str(int(seconds) / 6)
            seconds_to_float = str((float(whole_mins + seconds)) / 600)
            result = (int(whole_num) + float(seconds_to_float))
            result_screen.delete(index1=1.0, index2=END)
            result_screen.insert(END, f"{result}")
            result_screen.tag_configure("right", justify='right')
            result_screen.tag_add("right", 1.0, "end")
