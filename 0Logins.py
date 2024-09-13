from tkinter import *

def get_login(win, username, password):
    username= username.get()
    password= password.get()

    HashingFile.hashLogin(win, username, password)

def Login():

    #wn.destroy()
    tlogin= Tk()
    tlogin.title("Welcome to the teacher log in page.")
    tlogin.geometry("500x180")
    tlogin.configure(background='lightpink2')

    guideMessage= Label(tlogin, text="Enter your username and password.")
    guideMessage.grid(row=0,column=0, columnspan=3, sticky="W",padx=10,pady=10)
    guideMessage.config(font=("",14))


    usernameLabel= Label(tlogin, text="Username")
    usernameLabel.grid(row=1,column=0, padx=10,pady=10, sticky="W")

    passLabel= Label(tlogin, text="Password")
    passLabel.grid(row=2,column=0,padx=10,pady=10,sticky="W")

    usernameEntry= Entry(tlogin,width="40")
    usernameEntry.grid(row=1,column=1,padx=10,pady=10, sticky="E")

    passwordEntry = Entry(tlogin, width="40")
    passwordEntry.grid(row=2, column=1, padx=10, pady=10, sticky="E")

    clearButton = Button(tlogin, text="Clear", width=12, command=lambda: clearBoxes(tlogin, usernameEntry, passwordEntry))
    clearButton.grid(row=3, column=1, padx=10, pady=10)

    enterButton = Button(tlogin, text="Enter", width=12, command=lambda: get_login(form, usernameEntry, passwordEntry))
    enterButton.grid(row=3, column=2, padx=10, pady=10)

    exitButton = Button(tlogin, text="Exit", width=12, command=quit)
    exitButton.grid(row=3, column=0, padx=10, pady=10)

    mainloop()

def clearBoxes(Login,usernameEntry, passwordEntry):
    usernameEntry.delete(0,"end")
    passwordEntry.delete(0,"end")
    usernameEntry.focus()




Login()