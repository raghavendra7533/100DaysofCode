## Challenge 1 - Add a high score to the snake game
[[Day 20 and Day 21 - Snake Game]]
- Add another attribute to the scoreboard called `self.highscore`
- remove the game_over function from the scoreboard and add another function called high_score
- Add an if loop which checks if the score is higher than the high_score, if yes then reassign the value of high score to score and write 'New high Score!!' else write 'game over'
	- use `with open("data.txt) as f:"` and rewrite the data in the file to the high_score.

## File Paths
### Absolute File Paths
- Absolute file paths always starts off relative to the root.
- The root folder is usually the "origin" folder. In PCs it is the 'C' drive. 

>[!tip]- Example
>`/Work/Project/hola.docx`

### Relative File Paths
- If we are in the working directory and want to access a file in that or in that hierarchal directory we use `./talk.ppt` if we have to use a file inside a directory.
- While we use `../report.docx` to access a file in the parent directory.
- If we are in the same hierarchal level as the file we want to access we don't use any forward slashes.

>[!tip]- Example
>- `../` to go to the parent directory
>- no slashes if the file is in the same directory

## Mail Merge
### Declaring the placeholder Variable
- While we replace the names of the invitee in the txt file we should declare the Placeholder where the data should be replaced.
- The txt file with the names is given and all the names are in individual lines.
### Reading all the lines from the file
- Reading all the lines from the file and appending the same to a list.
- And iterating through the list and replacing the name with the PLACEHOLDER
### Creating a new file 
- After replacing the name, using the `with open(f"{name}.txt", "w) as file:"` we create a new file and update the file with the letter data.
```py
PLACEHOLDER = '[name]'  
  
  
with open("./Input/Names/invited_names.txt") as input_file:  
    names = input_file.readlines()  
  
list_names = []  
for name in names:  
    list_names.append(name.strip())  
  
with open("./Input/Letters/starting_letter.txt") as input_letter:  
    letter = input_letter.read()  
    letter = letter.strip()  
    for name in list_names:  
        new_letter = letter.replace(PLACEHOLDER, name)  
        with open(f"./Output/ReadyToSend/{name}.txt", "w") as output_file:  
            output_file.write(new_letter)
```

```txt
Dear [name],  
You are invited to my birthday this Saturday.  
Hope you can make it!  
Raghavendra
```

```txt
Aang  
Zuko  
Appa  
Katara  
Sokka  
Momo  
Uncle Iroh  
Toph
```
