# Day 33 - International Space Station Overhead Notifier
#### References
1. [[Day 27 - Tkinter, *args, **kwargs and creating GUI Programs]]
2. [[Status Codes]]
3. [[APIs MOC]]
## API (Application Programming Interfaces)
An Application Programming Interface (API) is a set of commands, functions, protocols and objects that programmers can use to create software or interact with an external system.
- API normally returns a json object
- API can also return a xml

## Requests library
Requests library is used to send http requests in python. To send a request we should use `requests.get(url=<url>)` and store it to a variable.

>[!error]- Note
>When we try to print this, we get the response to be `<response [200]>` and not the json

Refer [[Status Codes]] to know more about it, further [visit this website](httpstatuses.com) to know more
### raise_for_status()
This method returns a Exception with status code and what it means

## Challenge 1: Kanye Quote Machine 

1. Get the response
2. Get the text from the json response
3. item config the canvas text to show the quote
```py
from tkinter import *  
import requests  
  
  
def get_quote():  
    kanye_quote = requests.get(url="https://api.kanye.rest")  
    kanye_quote_text = kanye_quote.json()['quote']  
    canvas.itemconfig(quote_text, text=kanye_quote_text)  
  
  
window = Tk()  
window.title("Kanye Says...")  
window.config(padx=50, pady=50)  
  
canvas = Canvas(width=300, height=414)  
background_img = PhotoImage(file="background.png")  
canvas.create_image(150, 207, image=background_img)  
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")  
canvas.grid(row=0, column=0)  
  
kanye_img = PhotoImage(file="kanye.png")  
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)  
kanye_button.grid(row=1, column=0)  
  
  
  
window.mainloop()
```

## Challenge 2 : Get the sunrise and the sunset times
Website URL : [sunrise-sunset](https://sunrise-sunset.org) 
API URL : [API sunrise-sunset](https://api.sunrise-sunset.org/json)
Params : lat, long, date
