import tkinter


window = tkinter.Tk()
window.title("My first GUI Application")
window.minsize(500, 300)
my_label = tkinter.Label(text="I am a Label", font=("Arial", 15, "bold"))
my_label.pack(side="top")

window.mainloop()