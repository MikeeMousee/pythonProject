from tkinter import *

def Tlogin():

    wn.destroy()
    tlogin= Tk()
    tlogin.title("Welcome to the teacher log in page.")
    tlogin.geometry("500x180")

    teacherWelcome= Label(form, text="Welcome to the teacher log in.")
    teacherWelcome.grid(row=0,column=0, columnspan=3, sticky="W",padx=10,pady=10)

    teacherLabel= Lable(form, text="Teacher username")
    teacherLabel.grid(row=1,column=0, padx=10,pady=10, sticky="W")

    passLabel= Label(form, text="Password")
    mainwindow()