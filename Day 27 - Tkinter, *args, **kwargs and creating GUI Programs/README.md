#### References
1. [[Day 16 - OOP]]
2. [[Methods and Objects of Tkinter]]
3. [[Day 18 - Python Turtle and Extracting colors from an image]]


>[!info] Methods of Tkinter
>Refer [[Methods and Objects of Tkinter]]
>

- `tkinter` is a preinstalled module in python. 
- Like the `screen` in `turtle` we have to initialise `window` in Tkinter.

```py
import tkinter  
  
  
window = tkinter.Tk()  
window.title("My first GUI Application")  
window.minsize(500, 300)  
my_label = tkinter.Label(text="I am a Label", font=("Arial", 15, "bold"))  
my_label.pack(side="top")  
  
window.mainloop()
```


## Arguments with default values
When we declare functions, we also declare the arguments that need to be passed to the function, but when the value of the arguments doesn't change that often, we can declare default values.
```py
def my_function(a=1, b=2, c=3):
	a = a + 1
	b = b + 1
	c = c + 1

# if the value of the arguments doesn't change:
my_function()

# if for example the value of b needs to be changed
my_function(b=4)
# here the value of a and c remains the same
```

## Unlimited Arguments
If we use `*args` we can pass unlimited number of arguments.

### Challenge 1 : Create a function called add and return the sum of the numbers passed
```py
def add(*args):  
    sum1 = 0  
    for n in args:  
        sum1 = sum1 + n  
    return sum1  
  
  
print(add(2, 3, 4, 5343838498274))
```

>[!success]- Output
>5343838498283

>[!info]- Note
>`args` inside the class returns a tuple.

^ba6982

## `**`kwargs (Keyword Arguments)

- While args returns a tuple [[#^ba6982]] `**kwargs` returns a dict.
```py
def calculate(**kwargs):
	print(kwargs)

calculate(add=3, sub=2)
``` 

>[!success]- Output
>`{"add":3, "sub": 2}`


## Buttons, Entry and Setting Component Options

```py
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
    my_label["text"] = "Button got clicked"  


def reset():  
    my_label["text"] = "New Text"  
  
  
# Button  
button = Button(text="Click me", command=button_clicked)  
button2 = Button(text="Reset", command=reset)  
# command executes a function when triggered  

button.pack()  
button2.pack()  

# Entry
input = Entry()
input.pack()

window.mainloop()
```

## Tkinter Layout Managers
### Pack
Pack arranges each of the elements next to each other.
### Place
Place is all about precise positioning.
`my_label.place(x=0, y=0)`
### Grid
Grid is relative to other widgets using the grid.
```py
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
my_label.grid(column=0, row=0)

# my_label["text"] and my_label.config does the same thing its just 2 ways to do the same thing  


# Event Listener function  
def button_clicked():  
    my_label["text"] = "Button got clicked"  


def reset():  
    my_label["text"] = "New Text"  
  
  
# Button  
button = Button(text="Click me", command=button_clicked)  
button2 = Button(text="Reset", command=reset)  
button.grid(column=1, row=1)
# command executes a function when triggered  

button.pack()  
button2.pack()  

# Entry
input = Entry()
input.pack()

window.mainloop()
```

## Project : Miles to Kms Converter
```py
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
```
