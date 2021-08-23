from tkinter import *
import tkinter as tk
from tkinter import messagebox


w = Tk()
w.geometry("800x300")
title = "PSE Stock Average Price Calculator"
w.title(title)
# w.eval('tk::PlaceWindow . left')

Label(w,text="Quote").grid(column=0,row=0, pady=10)
quote_txt = Entry(w)
quote_txt.grid(column=1,row=0, pady=10)
quote_txt.focus()

Label(w,text="Price").grid(column=0,row=1, pady=10)
price = Entry(w)
price.grid(column=1,row=1, pady=10)

Label(w, text="Average Price").grid(column=0,row=2, pady=10)
ave_price = Entry(w)
ave_price.grid(column=1,row=2, pady=10)

Label(w, text="Existing Shares").grid(column=0,row=3, pady=10)
exist_shares = Entry(w)
exist_shares.grid(column=1,row=3, pady=10)

Label(w, text="Want to buy Shares").grid(column=0,row=4, pady=10)
want_shares = Entry(w)
want_shares.grid(column=1,row=4, pady=10)

def compute():
    print("hello")

tk.Button(w,text="Submit",command=compute).grid(column=0,row=5,columnspan=2)

w.mainloop()