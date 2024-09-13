import hashlib

def hash_input(inputvar):  # hashes any input
    # Hash the password using SHA-256 (for demonstration purposes)
    return hashlib.sha256(inputvar.encode('utf-8')).hexdigest()

def hashLogin(win, userVar, passVar):
    # if username and password are valid:
    #if validation.validuser(userVar) and validation.validpass(passVar):
        passVar = hash_input(passVar)  # hash the password
        # serach if the username and password matched in database
        if SQLdatabase.searchUser(userVar, passVar): # if match
            messagebox.showinfo("Success", "welcome to my app. ... chose an option from main menu  ") # show welcome message
        else:
            messagebox.showinfo("User not found", "This account doesn't exist. Enter a different account or get a new one.") # if not match show try again message
            win.destroy() # close the window h
            main.main() # restart
    #else:

        #messagebox.showinfo("Invalid username or password","Password must be at least  8 characters."
                                       #" User name must be at least 4 charactersname ") # if invalid password and username
        #win.destroy() # close the window
        #main.main() # restart
