from tkinter import *
from tkinter import messagebox
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def make_one():

    # print("Welcome to the PyPassword Generator!")
    no_letters = random.randint(8, 10)
    no_symbols = random.randint(2, 4)
    no_numbers = random.randint(2, 4)

    password = ""
    for i in range(1, no_letters+1):
        p = random.choice(letters)
        password = password+p
    for i in range(1, no_symbols+1):
        p = random.choice(symbols)
        password = password+p
    for i in range(1, no_numbers+1):
        p = random.choice(numbers)
        password = password+p

    password_entry.insert(END, string=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_entry():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    entry = f"{website} | {email_username} | {password} \n"

    if len(website) == 0 or len(password) == 0 :
        messagebox.showerror(title="Errorr", message="Some field is left empty.")

    else:
        is_sure = messagebox.askokcancel(title=f"{website}", message=f"The details entered are: \n\nEmail | Username: {email_username} \nPassword: {password}")
        if is_sure:
            with open("idk.txt", "a") as f:
                f.write(entry)
            website_entry.delete(first=0, last="end")
            password_entry.delete(first=0, last="end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("courier", 13, "bold"))
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", font=("courier", 13, "bold"))
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("courier", 13, "bold"))
password_label.grid(column=0, row=3)

website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
email_username_entry = Entry(width=51)
email_username_entry.insert(END, string="Jalvin@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=make_one)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="add", width=44, command=save_entry)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
