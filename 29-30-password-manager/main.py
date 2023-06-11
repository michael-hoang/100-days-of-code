from tkinter import *  # Only imports all of classes and constants, not messagebox
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    ent_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def format_text():
    """Returns formatted website, email/username, and password entries as a \
single string."""
    website = ent_website.get()
    email = ent_email.get()
    password = ent_pass.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields \
empty!")
    else:
        # text = f"{website} | {email} | {password}\n"
        return website, email, password


def save():
    """Writes password to file called data.txt."""
    website, email, password = format_text()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # try:
    #     f = open("data.json", "r")
    # except FileNotFoundError:
    #     f = open("data.json", "w")
    #     data = new_data
    # else:
    #     data = json.load(f)  # Reading old data
    #     data.update(new_data)  # Updating old data with new data
    #     f = open("data.json", "w")
    # finally:
    #     json.dump(data, f, indent=4)  # Saving updated data
    #     f.close()


    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open("data.json", "w") as f:
            json.dump(new_data, f, indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)
    finally:
        # Clear entries
        ent_website.delete(0, END)
        # ent_email.delete(0, END)
        ent_pass.delete(0, END)


# ---------------------------- FIND PASSWORD --------------------------- #

def find_password():
    website = ent_website.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    # except KeyError:
    #     messagebox.showinfo(title="Oops", message="No details for the website exists.")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists.")
    

# ---------------------------- UI SETUP ------------------------------- #
# Create root window
root = Tk()
root.title("Password Manager")
root.config(padx=40, pady=40)

# Create Canvas
canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Create Labels
lab_website = Label(text="Website:")
lab_email = Label(text="Email/Username:")
lab_pass = Label(text="Password:")

lab_website.grid(column=0, row=1)
lab_email.grid(column=0, row=2)
lab_pass.grid(column=0, row=3)

# Create Entries
ent_website = Entry()
ent_website.focus()  # Focus cursor on Website entry bar
ent_email = Entry()
ent_email.insert(0, "angela@gmail.com")
ent_pass = Entry()

ent_website.grid(column=1, row=1, columnspan=1, sticky="EW")
ent_email.grid(column=1, row=2, columnspan=2, sticky="EW")
ent_pass.grid(column=1, row=3, sticky="EW")

# Create Buttons
but_genPass = Button(text="Generate Password", command=generate_password)
but_add = Button(text="Add", command=save)
but_genPass.grid(column=2, row=3)
but_add.grid(column=1, row=4, columnspan=2, sticky="EW")

# Create Search Button
but_search = Button(text="Search", command=find_password)
but_search.grid(column=2, row=1, sticky="EW")

# Create main event loop
root.mainloop()
