# C:\Program Files\Python310\python.exe
from tkinter import *

def back(wn):
    wn.destroy()
    main()

def main():
    win1=Tk()
    win1.title("Welcome")
    win1.geometry("500x180")
    win1.configure(background='turquoise3')

    titleLabel= Label(win1, text="Welcome to Mikee's log in page.")
    titleLabel.grid(row=0, column=0, columnspan=4, sticky="NESW", pady=10, padx=10)

    exitButton= Button(win1, text="Exit", width=12, command= quit)
    exitButton.grid(row=1, column=0, padx=10, pady=10)

    loginButton= Button(win1,text="Log in", width=12, command=lambda:login())
    loginButton.grid(row=1, column=1, padx=10,pady=10)

    mainloop()

main()

