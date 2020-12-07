from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Calculator Demo')
root.iconbitmap('calculator_yellow.ico')
root.resizable(0, 0)

e = Entry(root, width=40, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_clicK(num):
    now = e.get()
    e.delete(0, END)
    e.insert(0, str(now) + str(num))


def button_add():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0, END)


def button_sub():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)


def button_mul():
    first_num = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    e.delete(0, END)


def button_div():
    first_num = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    e.delete(0, END)


def button_sqrt(sqrt):
    global sqrt1
    sqrt1 = e.get()
    global math
    math = 'squareroot'
    e.delete(0, END)


def button_equal():
    second_num = e.get()
    e.delete(0, END)
    global s_num
    s_num = int(second_num)
    if math == 'addition':
        e.insert(0, f_num + s_num)
    elif math == 'subtraction':
        e.insert(0, f_num - s_num)
    elif math == 'division':
        e.insert(0, f_num / s_num)
    elif math == 'multiplication':
        e.insert(0, f_num * s_num)
    elif math == 'squareroot':
        e.insert(0, sqrt1.sqrt)


def button_clear():
    e.delete(0, END)


button_1 = Button(root, text='1', padx=20, pady=10,
                  command=lambda: button_clicK(1))
button_2 = Button(root, text='2', padx=20, pady=10,
                  command=lambda: button_clicK(2))
button_3 = Button(root, text='3', padx=20, pady=10,
                  command=lambda: button_clicK(3))
button_4 = Button(root, text='4', padx=20, pady=10,
                  command=lambda: button_clicK(4))
button_5 = Button(root, text='5', padx=20, pady=10,
                  command=lambda: button_clicK(5))
button_6 = Button(root, text='6', padx=20, pady=10,
                  command=lambda: button_clicK(6))
button_7 = Button(root, text='7', padx=20, pady=10,
                  command=lambda: button_clicK(7))
button_8 = Button(root, text='8', padx=20, pady=10,
                  command=lambda: button_clicK(8))
button_9 = Button(root, text='9', padx=20, pady=10,
                  command=lambda: button_clicK(9))
button_0 = Button(root, text='0', padx=20, pady=10,
                  command=lambda: button_clicK(0))
button_add = Button(root, text='+', padx=20, pady=10, command=button_add)
button_sub = Button(root, text='-', padx=20, pady=10, command=button_sub)
button_div = Button(root, text='/', padx=20, pady=10, command=button_div)
button_mul = Button(root, text='*', padx=20, pady=10, command=button_mul)
button_equal = Button(root, text='=', padx=20, pady=10, command=button_equal)
button_clear = Button(root, text='CLS', padx=20, pady=10, command=button_clear)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1,)
button_clear.grid(row=4, column=0)

button_add.grid(row=3, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=1, column=3)
button_div.grid(row=4, column=2)
button_equal.grid(row=4, column=3)


root.mainloop()
