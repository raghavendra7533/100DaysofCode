## Import `tkinter`
`from tkinter import *`

## Create the Window
[[Methods and Objects of Tkinter]]

## Create the Canvas
[[Methods and Objects of Tkinter]]

>[!info]-
>I had to add `fill="black"` `attribute to canvas.create_text()`


## Create a PhotoImage for the 'right' and 'wrong' button

```py
# Wrong Button
cross_image=PhotoImage(file="images/wrong.png")  
unknown_button = Button(image=cross_image, highlightthickness=0)  
unknown_button.grid(row=1, column=0)
```

```py
# Right Button
check_image=PhotoImage(file="images/right.png")  
unknown_button = Button(image=check_image, highlightthickness=0)  
unknown_button.grid(row=1, column=1)
```

## Add a command to the buttons
Add commands to the button, which is methods to be executed on-click.

## Full Code
```py
from tkinter import *  
import pandas  
import random  
  
BACKGROUND_COLOR = "#B1DDC6"  
  
data = pandas.read_csv("data/french_words.csv")  
to_learn = data.to_dict(orient="records")  
print(to_learn)  
current_card = {}  
  
  
def next_card():  
    global current_card, flip_timer  
    window.after_cancel(flip_timer)  
    current_card = random.choice(to_learn)  
    canvas.itemconfig(card_title, text="French", fill="black")  
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")  
    canvas.itemconfig(card_background, image=card_front_img)  
    flip_timer = window.after(3000, func=flip_card)  
  
  
  
def flip_card():  
    canvas.itemconfig(card_title, text="English", fill="white")  
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")  
    canvas.itemconfig(card_background, image=card_back_img)  
  
def is_known():  
    to_learn.remove(current_card)  
    data = pandas.DataFrame(to_learn)  
    data.to_csv("data/words_to_learn")  
    next_card()  
  
  
window = Tk()  
window.title("Flashy")  
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)  
flip_timer = window.after(3000, func=flip_card)  
  
canvas = Canvas(width=800, height=526)  
card_front_img = PhotoImage(file="images/card_front.png")  
card_back_img = PhotoImage(file="images/card_back.png")  
card_background = canvas.create_image(400, 263, image=card_front_img)  
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")  
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"), fill="black")  
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)  
canvas.grid(row=0, column=0, columnspan=2)  
  
cross_image=PhotoImage(file="images/wrong.png")  
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)  
unknown_button.grid(row=1, column=0)  
  
check_image=PhotoImage(file="images/right.png")  
know_button = Button(image=check_image, highlightthickness=0, command=is_known)  
know_button.grid(row=1, column=1)  
  
  
  
window.mainloop()
```
