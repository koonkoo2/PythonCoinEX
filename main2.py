import tkinter
from tkinter import *


root = Tk()
root.title("CoinExCalculator")
root.geometry("400x350")

def Calculation():
    thb = int(THBentry.get())

    thb_usdm = thb*0.028
    thb_eurm = thb*0.026
    thb_yenm = thb*4.12
    thb_cnym = thb*0.20
    Label(root, text=f"THB to USD = {thb_usdm}", font="arial 10").place(x=50, y=80)
    Label(root, text=f"THB to EUR = {thb_eurm}", font="arial 10").place(x=50, y=120)
    Label(root, text=f"THB to YEN = {thb_yenm}", font="arial 10").place(x=50, y=160)
    Label(root, text=f"THB to CNY = {thb_cnym}", font="arial 10").place(x=50, y=200)

sub1 = Label(root, text="THB:", font="arial 10")
sub1.place(x=100, y=20)

THBentry = Entry(root, font="arial 15", width=15)
THBentry.place(x=140, y=20)

Button(root, text="Calculate", font="arial 15", bg="white", bd=10, command=Calculation).place(x=145, y=250)

root.mainloop()
