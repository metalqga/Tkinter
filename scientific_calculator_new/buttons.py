from functions import *
from body import root
from tkinter import *
shift = 0



def shift_click():
    global shift
    if shift % 2 == 0:
        button_x1.place_forget()
        button_x11.place(x=0, y=210)
        button_ncr.place_forget()
        button_npr.place(x=55, y=210)
        button_mode.place_forget()
        button_clr.place(x=230, y=175)
        button_pol.place_forget()
        button_rec.place(x=230, y=210)
        button_cd.place_forget()
        button_abc.place(x=0, y=245)
        button_powerx.place_forget()
        button_sqrtx.place(x=172, y=245)
        button_log.place_forget()
        button_10x.place(x=230, y=245)
        button_ln.place_forget()
        button_ex.place(x=290, y=245)
        button_degrees.place_forget()
        button_arrowdeg.place(x=55, y=280)
        button_sin.place_forget()
        button_sin1.place(x=172, y=280)
        button_cos.place_forget()
        button_cos1.place(x=230, y=280)
        button_tan.place_forget()
        button_tan1.place(x=290, y=280)
        button_rcl.place_forget()
        button_sto.place(x=0, y=315)
        button_eng.place_forget()
        button_engarrow.place(x=55, y=315)
        button_decimal.grid_forget()
        button_ran.grid(row=10, column=1)
        # removing rnd functionality
        # button_0.grid_forget()
        # button_rnd.grid(row=10, column=0)
        button_exp.grid_forget()
        button_pi.grid(row=10, column=2)
        button_mp.place_forget()
        button_mm.place(x=290, y=315)
        button_on.place_forget()
        button_off.place(x=290, y=175)

    else:
        button_x11.place_forget()
        button_x1.place(x=0, y=210)
        button_npr.place_forget()
        button_ncr.place(x=55, y=210)
        button_clr.place_forget()
        button_mode.place(x=230, y=175)
        button_rec.place_forget()
        button_pol.place(x=230, y=210)
        button_abc.place_forget()
        button_cd.place(x=0, y=245)
        button_sqrtx.place_forget()
        button_powerx.place(x=172, y=245)
        button_10x.place_forget()
        button_log.place(x=230, y=245)
        button_ex.place_forget()
        button_ln.place(x=290, y=245)
        button_arrowdeg.place_forget()
        button_degrees.place(x=55, y=280)
        button_sin1.place_forget()
        button_sin.place(x=172, y=280)
        button_cos1.place_forget()
        button_cos.place(x=230, y=280)
        button_tan1.place_forget()
        button_tan.place(x=290, y=280)
        button_sto.place_forget()
        button_rcl.place(x=0, y=315)
        button_engarrow.place_forget()
        button_eng.place(x=55, y=315)
        button_ran.grid_forget()
        button_decimal.grid(row=10, column=1)
        # button_rnd.grid_forget()
        button_0.grid(row=10, column=0)
        button_pi.grid_forget()
        button_exp.grid(row=10, column=2)
        button_mm.place_forget()
        button_mp.place(x=290, y=315)
        button_off.place_forget()
        button_on.place(x=290, y=175)
    shift += 1



# Define Buttons
button_1 = Button(root, text="1", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(1))
button_2 = Button(root, text="2", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(2))
button_3 = Button(root, text="3", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(3))
button_4 = Button(root, text="4", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(4))
button_5 = Button(root, text="5", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(5))
button_6 = Button(root, text="6", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(6))
button_7 = Button(root, text="7", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(7))
button_8 = Button(root, text="8", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(8))
button_9 = Button(root, text="9", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(9))
button_0 = Button(root, text="0", font=('Times', '24', 'bold'), borderwidth=5, padx=7, pady=5,
                  command=lambda: button_click(0))

# + - * / . =  clr
button_plus = Button(root, text="+", font=('Times', '12', 'bold'), borderwidth=5, padx=20, pady=20,
                     command=lambda: button_click("+"))
button_minus = Button(root, text="-", font=('Times', '12', 'bold'), borderwidth=5, padx=23, pady=20,
                      command=lambda: button_click("-"))
button_mul = Button(root, text="*", font=('Times', '12', 'bold'), borderwidth=5, padx=20, pady=20,
                    command=lambda: button_click("*"))
button_div = Button(root, text="/", font=('Times', '12', 'bold'), borderwidth=5, padx=23, pady=20,
                    command=lambda: button_click("/"))
button_decimal = Button(root, text=".", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=3, pady=19,
                        command=lambda: button_click("."))
button_equal = Button(root, text="=", font=('Times', '12', 'bold'), borderwidth=5, padx=20, pady=18,
                      command=expression_parser)
button_ac = Button(root, text="AC", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=5, pady=18, command=ce)
button_del = Button(root, text="DEL", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=5, pady=18,
                    command=delete)

# special buttons
button_sqrt = Button(root, text="√", font=('Times', '12'), width=5, borderwidth=1, padx=1, pady=0,
                     command=lambda: button_click("sqrt("))
button_mrc = Button(root, text="MC", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=8,
                    command=rclmem)
button_mp = Button(root, text="M+", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                   command=memoryplus)
button_mm = Button(root, text="M-", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                   command=memoryminus)
button_parenth = Button(root, text="(", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=lambda: button_click("("))
button_parenth1 = Button(root, text=")", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                         command=lambda: button_click(")"))
button_sin = Button(root, text="sin", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("sind("))
button_cos = Button(root, text="cos", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("cosd("))
button_tan = Button(root, text="tan", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("tand("))
button_power2 = Button(root, text="x²", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                       command=lambda: button_click("^2"))
button_power3 = Button(root, text="x³", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                       command=lambda: button_click("^3"))
button_shift = Button(root, text="SHIFT", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                      command=shift_click)
button_alpha = Button(root, text="ALPHA", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                      command=expression_parser)
button_mode = Button(root, text="MODE", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                     command=mode)
button_on = Button(root, text="ON", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=on)
button_off = Button(root, text="OFF", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=exit)
button_x1 = Button(root, text="X(-1)", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                   command=lambda: button_click("^(-1)"))
button_x11 = Button(root, text="X!", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("fac("))
button_cd = Button(root, text="d/c", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=cd)
button_minus_parenth = Button(root, text="(-)", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                              command=lambda: button_click("-"))
button_rcl = Button(root, text="RCL", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=rclmem)
button_ncr = Button(root, text="nCr", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_degrees = Button(root, text="º'''", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=to_degrees)  # button_click("º"))
button_eng = Button(root, text="ENG", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=eng)
button_hyp = Button(root, text="hyp", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_powerx = Button(root, text="^", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                       command=lambda: button_click("^"))
button_pol = Button(root, text="Pol(", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("pol("))
button_log = Button(root, text="log", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("log( ,10)"))
button_ln = Button(root, text="ln", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                   command=lambda: button_click("log("))
button_exp = Button(root, text="EXP", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=3, pady=19,
                    command=lambda: button_click("10^"))
button_ans = Button(root, text="Ans", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=5, pady=18,
                    command=lambda: ans())
button_comma = Button(root, text=",", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                      command=lambda: button_click(","))
button_arrow_l = Button(root, text="◄", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=lambda: move_cursor("◄"))
button_arrow_r = Button(root, text="►", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=lambda: move_cursor("►"))
button_arrow_d = Button(root, text="▼", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=lambda: eq_memory(-1))
button_arrow_u = Button(root, text="▲", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                        command=lambda: eq_memory(1))

# shifted buttons
button_npr = Button(root, text="nPr", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_clr = Button(root, text="CLR", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_rec = Button(root, text="Rec(", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("rec("))
button_abc = Button(root, text="ab/c", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_sqrtx = Button(root, text="x√", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_ex = Button(root, text="e^x", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                   command=lambda: button_click("E^"))
button_10x = Button(root, text="10^x", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                    command=lambda: button_click("10^"))
button_arrowdeg = Button(root, text="<-", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                         command=x1)
button_sin1 = Button(root, text="asin", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                     command=lambda: button_click("asind("))
button_cos1 = Button(root, text="acos", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                     command=lambda: button_click("acosd("))
button_tan1 = Button(root, text="atan", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                     command=lambda: button_click("atand("))
button_sto = Button(root, text="STO", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0, command=x1)
button_engarrow = Button(root, text="<-", font=('Times', '12', 'bold'), width=5, borderwidth=1, padx=0, pady=0,
                         command=x1)
button_ran = Button(root, text="Ran#", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=3, pady=19,
                    command=lambda: randomnum())
# button_rnd = Button(root, text="Rnd", font=('Times', '12', 'bold'), borderwidth=5, padx=8, pady=20, command=x1)

button_pi = Button(root, text="π", font=('Times', '12', 'bold'), width=5, borderwidth=5, padx=3, pady=19,
                   command=lambda: button_click("PI"))


# memory indicator TO refine this indicator
button_memory = Button(root, text="M", font=('Times', '10', 'bold'), background="white", state=DISABLED)
button_radians = Button(root, text="RAD", font=('Times', '10', 'bold'), background="white", state=DISABLED)

