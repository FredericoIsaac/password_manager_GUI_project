from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
MAIL = "mail@mail.com"

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="No Data", message="No details for the website exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = letters_list + numbers_list + symbols_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    username = email_username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                              f"\nPassword: {password} \n Is this ok to save?")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # Reading old data
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)

            website_entry.delete(0, "end")
            email_username_entry.delete(0, "end")
            password_entry.delete(0, "end")

            email_username_entry.insert(END, MAIL)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Image in the background
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_logo)

# Layout
website_label = Label(text="Website:", bg="white")
email_username_label = Label(text="Email/Username:", bg="white")
password_label = Label(text="Password:", bg="white")

website_entry = Entry(width=23)
website_entry.focus()
email_username_entry = Entry(width=40)
email_username_entry.insert(END, MAIL)
password_entry = Entry(width=23)

generate_password_btn = Button(text="Generate Password", highlightthickness=0, bg="white", command=generate_password)
add_btn = Button(text="Add", highlightthickness=0, width=36, bg="white", command=save)
search_button = Button(text="Search", highlightthickness=0, width=15, bg="white", command=find_password)

# Grid system
canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
email_username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry.grid(column=1, row=1, sticky=W)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky=W)
password_entry.grid(column=1, row=3, sticky=W)

generate_password_btn.grid(column=1, row=3, columnspan=2, sticky=E)
add_btn.grid(column=1, row=4, columnspan=2, sticky=W)
search_button.grid(column=1, row=1, columnspan=2, sticky=E)

window.mainloop()
