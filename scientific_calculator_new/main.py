from buttons import *
from functions import expression_parser
#from my_parser import Parser
from fractions import Fraction
#import pyglet
#pyglet.font.add_file('LCDMU___.ttf')


# Put buttons on the grid
button_1.grid(row=9, column=0)
button_2.grid(row=9, column=1)
button_3.grid(row=9, column=2)
button_4.grid(row=8, column=0)
button_5.grid(row=8, column=1)
button_6.grid(row=8, column=2)
button_7.grid(row=7, column=0)
button_8.grid(row=7, column=1)
button_9.grid(row=7, column=2)
button_0.grid(row=10, column=0)
button_decimal.grid(row=10, column=1)
button_del.grid(row=7, column=3)
button_ac.grid(row=7, column=4)
button_mul.grid(row=8, column=3)
button_div.grid(row=8, column=4)
button_plus.grid(row=9, column=3)
button_minus.grid(row=9, column=4)
button_ans.grid(row=10, column=3)
button_exp.grid(row=10, column=2)
button_equal.grid(row=10, column=4)



# function keys with PLACE()
# row 0
button_shift.place(x=0, y=175)
button_alpha.place(x=55, y=175)
button_arrow_l.place(x=115, y=175)
button_arrow_r.place(x=170, y=175)
button_mode.place(x=230, y=175)
button_on.place(x=290, y=175)
# row 1
button_arrow_d.place(x=115, y=210)
button_arrow_u.place(x=170, y=210)
button_x1.place(x=0, y=210)
button_ncr.place(x=55, y=210)
button_pol.place(x=230, y=210)
button_power3.place(x=290, y=210)
# row 2
button_cd.place(x=0, y=245)
button_sqrt.place(x=55, y=245)
button_power2.place(x=113, y=245)
button_powerx.place(x=172, y=245)
button_log.place(x=230, y=245)
button_ln.place(x=290, y=245)
# row 3
button_minus_parenth.place(x=0, y=280)
button_degrees.place(x=55, y=280)
button_hyp.place(x=113, y=280)
button_sin.place(x=172, y=280)
button_cos.place(x=230, y=280)
button_tan.place(x=290, y=280)
# row 4
button_rcl.place(x=0, y=315)
button_eng.place(x=55, y=315)
button_parenth.place(x=113, y=315)
button_parenth1.place(x=172, y=315)
button_comma.place(x=230, y=315)
button_mp.place(x=290, y=315)

# evaluate at ENTER key
root.bind("<KeyPress-Return>", expression_parser)


root.mainloop()
