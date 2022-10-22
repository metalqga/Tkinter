from tkinter import *


root = Tk()
root.minsize(360, 700)
root.maxsize(360, 700)
root.title("A scientific Python Calculator using Tkinter")


# input screen
e = Text(root, background="#d3d3d3", font=('Times', '28', 'bold'), height=2, width=17, borderwidth=10)
e.grid(row=0, column=0, columnspan=10, rowspan=1, padx=10, pady=0)
#set the cursor blinking in input text box
e.focus_set()
# result screen
result_screen = Text(root, background="#d3d3d3", font=('Times', '32', 'bold'), height=1, width=14, borderwidth=10)
result_screen.grid(row=1, column=0, columnspan=10, rowspan=1, padx=10, pady=0)
#align buttons with grid() under the buttons with place()
canvas=Canvas(root, width=1, height=1)
canvas.grid(row=3, column=0, padx=0, pady=100)