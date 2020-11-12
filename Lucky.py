from tkinter import *
from tkinter import messagebox
from random import choice

__author__ = "Buse Savcı"
__license__ = "GNU General Public License"
__version__ = "1.0.0"

top = Tk()
top.geometry("300x150")
top.configure(background='gray')


def dice_roll():
    msg = messagebox.showinfo("Random Number :", choice(range(6)))


def head_or_tail():
    msg = messagebox.showinfo("Result : ", choice(["Head", "Tail"]))


def rock_paper_scissors():
    msg = messagebox.showinfo("Result : ", choice(["Rock", "Paper", "Scissors"]))


B = Button(top, text="Dice Roll", command=dice_roll, bg='pink')
B.place(x=15, y=50)

B1 = Button(top, text="Head Or Tail", command=head_or_tail, bg='pink')
B1.place(x=85, y=50)

B2 = Button(top, text="Rock Paper Scissors", command=rock_paper_scissors, bg='pink')
B2.place(x=175, y=50)

top.mainloop()
