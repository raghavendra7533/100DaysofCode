from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# setting component options and config
my_label["text"] = "New Text"
my_label.config(text="New Text")


# my_label["text"] and my_label.config does the same thing its just 2 ways to do the same thing

# Event Listener function
def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text


# Button
button = Button(text="Click me", command=button_clicked)
# command executes a function when triggered

button.pack()

# Entry
input = Entry(width=10)
input.pack()

window.mainloop()
