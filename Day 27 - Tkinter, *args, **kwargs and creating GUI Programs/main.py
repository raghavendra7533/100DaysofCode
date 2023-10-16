from tkinter import *

window = Tk()
window.title("Mile to Kilometer Conversion")
window.minsize(width=300,height=300)


def convert():
    number = int(input.get())
    kms = number * 1.609344
    kms = round(kms)
    km_label["text"] = kms


input = Entry(width=10)
input.grid(column=1, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=1)
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0,row=3)
km_label = Label(text="")
km_label.grid(column=1, row=3)
km_unit_label = Label(text="km")
km_unit_label.grid(column=2, row=3)
button = Button(text="convert", command=convert)
button.grid(column=1, row=4)




window.mainloop()