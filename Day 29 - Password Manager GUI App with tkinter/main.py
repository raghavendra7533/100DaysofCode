from tkinter import *
import random
import string


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    characters = string.ascii_letters + string.digits
    random_password = ''.join(random.choice(characters) for _ in range(10))
    random_password_tv = StringVar()
    random_password_tv.set(random_password)
    password_input.config(textvariable=random_password_tv)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def store_password():
    ws = website_input.get()
    ps = password_input.get()
    un = username_input.get()
    n_data = f"{ws} | {un} | {ps} \n"
    with open("data.txt", "r") as f:
        data = f.readlines()
    data.append(n_data)
    with open("data.txt", "w") as f:
        for line in data:
            f.write(line)
    website_input.delete(0, END)
    password_input.delete(0, END)
    username_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas Setup
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)

# email Label and input
website_label = Label(text="Website", font=("Arial", 18, "normal"))
website_label.grid(column=0, row=2)
website_input = Entry(width=35)
website_input.grid(column=2, row=2, columnspan=2)

# Email/Password Label and input
username_label = Label(text="Username", font=("Arial", 18, "normal"))
username_label.grid(column=0, row=3)
username_input = Entry(width=35)
username_input.grid(column=2, row=3, columnspan=2)

# Password Label and input
password_label = Label(text="password", font=("Arial", 18, "normal"))
password_label.grid(column=0, row=4)
password_input = Entry(width=25)
password_input.grid(column=2, row=4)

# Generate Password button
generate_password = Button(text="Generate", font=("Arial", 12, "normal"), command=generate_password)
generate_password.grid(column=3, row=4)

# Add button
add_button = Button(text="Add", width=33, command=store_password)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
