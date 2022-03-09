from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered:\nEmail: {email} "
                                                                   f"\nPassword: {password}\n Is it ok?")

        if is_ok:
            try:
                with open("passwords.json", "r") as f:
                    data = json.load(f)
                    data.update(new_data)
            except json.decoder.JSONDecodeError:
                with open("passwords.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                with open("passwords.json", "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# --------------------------- SEARCH PASSWORD -------------------------- #


def search():
    search_website = website_entry.get().title()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="No data File Found.")
    else:
        if search_website in data.keys():
            email = data[search_website]["email"]
            password = data[search_website]["password"]
            messagebox.showinfo(title=search_website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {search_website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo_image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=17)
website_entry.grid(column=1, row=1, sticky="we")
website_entry.focus()
username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2, sticky="we")
username_entry.insert(0, "nkrocks@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="ew")
password_generator = Button(text="Generate Password", command=generate_password)
password_generator.grid(column=2, row=3, sticky="ew")
add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
