from tkinter import *
import tkinter as tk
from tkinter import messagebox


w = Tk()
w.geometry("800x300")
title = "PSE Stock Average Price Calculator"
w.title(title)
# w.eval('tk::PlaceWindow . left')

Label(w,text="Quote : ").grid(column=0,row=0)
quote_txt = Entry(w)
quote_txt.grid(column=1,row=0)
quote_txt.focus()

Label(w,text="Price : ").grid(column=0,row=1)
price = Entry(w)
price.grid(column=1,row=1)

Label(w, text="Average Price : ").grid(column=0,row=2)
ave_price = Entry(w)
ave_price.grid(column=1,row=2)

Label(w, text="Existing Shares : ").grid(column=0,row=3, pady=10)
exist_shares = Entry(w)
exist_shares.grid(column=1,row=3, pady=10)

Label(w, text="Want to buy Shares : ").grid(column=0,row=4, pady=10)
want_shares = Entry(w)
want_shares.grid(column=1,row=4, pady=10)

Label(w, text="Net + Commision : ").grid(column=3,row=0, pady=10)
Label(w, text="Forecasted Shares : ").grid(column=3,row=1, pady=10)
Label(w, text="Existing Amount Spent : ").grid(column=3,row=2, pady=10)
Label(w, text="Forecasted Amount Spent : ").grid(column=3,row=3, pady=10)
Label(w, text="Forecasted Average Price : ").grid(column=3,row=4, pady=10)


def compute():
    netcom = float(price.get()) * float(want_shares.get()) + int(25)
    f_shares = float(exist_shares.get()) + float(want_shares.get())
    exist_amount = float(ave_price.get()) * float(exist_shares.get())
    f_spent = exist_amount + netcom
    f_ave_price = f_spent / f_shares

    Label(w,text=netcom).grid(column=4,row=0, pady=10)
    Label(w,text=f_shares).grid(column=4,row=1, pady=10)
    Label(w,text=exist_amount).grid(column=4,row=2, pady=10)
    Label(w,text=f_spent).grid(column=4,row=3, pady=10)
    Label(w,text=f_ave_price).grid(column=4,row=4, pady=10)
    

tk.Button(w,text="Submit",command=compute,width=20).grid(column=0,row=5,columnspan=2)


w.mainloop()