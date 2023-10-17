
## Project : Pomodoro Timer
### UI Setup
1. Initialise the window
2. Define the title of the window to "Pomodoro Timer"
3. Config the window to have padding of 100 on the x-axis and 50 on the y-axis
4. Define [[#Canvas]] with width of 200 and height of 224
5. Canvas only takes "PhotoImage", so convert the tomato_img to a PhotoImage
6. Create a text in the canvas using "canvas.create_text()" and it takes args and kwargs args being the position of the text
7. Use the "Pack" method for it to appear
8. Create a timer label and check mark label
9. Create 2 buttons start and reset

### Countdown Mechanism
Counting down by changing the timer label when clicked on start
1. first define the count in start_timer
2. define count_min and divide it by 60 and floor it
3. count_sec is the mod of count and 60
4. if count