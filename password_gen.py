import random
from tkinter import messagebox
from tkinter import *

# Character string used for password generation
char_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def gen_passwd():
    """
    Try and except are used for error handling if the user does not enter all required fields.
    If any required fields are missing, an error message will be displayed.
    """
    try:
        # Get user inputs
        length = int(length_entry.get())  # Correctly use length_entry for password length
        repeat = int(repeat_entry.get())  # Correctly use repeat_entry for repetition option
    except ValueError:
        messagebox.showerror(message="Please fill in all required fields with valid numbers.")
        return  # Stops code execution if there's an error

    # Checking if the user allows repetition of characters in their password
    if repeat == 1:
        passwd = random.sample(char_string, length)  # Random sample without repetition
    else:
        passwd = random.choices(char_string, k=length)  # Random choices with repetition

    passwd = ''.join(passwd)  # Join list into a single string

    # Display the generated password
    passwd_v.set("Conjured Password: " + passwd)  # Update the password variable

# Creating the user interface (GUI) outside the function
passwd_gen = Tk()
passwd_gen.geometry("350x250")
passwd_gen.title("Noob Password Generator")

# Creating the title label
title_label = Label(passwd_gen, text='Noob Password Generator', font=('Ubuntu Mono', 14))
title_label.pack()

# Length of password label and entry
length_label = Label(passwd_gen, text='Enter length of password: ')
length_label.place(x=20, y=30)
length_entry = Entry(passwd_gen, width=3)
length_entry.place(x=190, y=30)

# Repetition label and entry
repeat_label = Label(passwd_gen, text='Repetition? 1 = no, 2 = yes')
repeat_label.place(x=20, y=60)
repeat_entry = Entry(passwd_gen, width=4)
repeat_entry.place(x=190, y=60)

# Button to generate password
passwd_btn = Button(passwd_gen, text="Generate Password", command=gen_passwd)
passwd_btn.place(x=100, y=100)

# Label to display the generated password
passwd_v = StringVar()  # Variable to hold the generated password
passwd_label = Entry(passwd_gen, bd=0, bg='gray85', textvariable=passwd_v, state="readonly")
passwd_label.place(x=10, y=140, height=50, width=320)

# Run the Tkinter main loop to display the window
passwd_gen.mainloop()