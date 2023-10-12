## List Comprehension

>[!note] List Comprehension
>List comprehension is unique to Python. It is not available in other Language. 

List is a case where we create a new list from an existing list. We were using a `for` loop for this until now.

### Using `for` loop
```py
numbers = [1, 2, 3]
new_list = []
for n in list:
	add_1 = n + 1
	new_list.append(add_1)
```

>[!success]- Output without List Comprehension
>`[2, 3, 4]`
### Using List Comprehension
```py
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)
```

>[!success]- Output with List Comprehension
>`[2, 3, 4]`
### List Comprehension in a `string`
```py
name = "Raghav"
new_list = [letter for letter in name]
```

>[!note]- What are Python Sequences?
>Things like `list`,  `range`, `string` and `tuple` are known as Python Sequences.

### Challenge 1 : Create a range between 1, 5

```py
range_list = [2 * num for num in range(1,5)]
```

>[!success]- Output
>`[2, 4, 6, 8]`

### Passing conditions
```py
names = ["Alex", "Beth", "Carolina", "Dave", "Freddie"]
short_names = [name for name in names if len(name) < 5]
```

>[!success]- Output
>`['Alex', 'Beth', 'Dave']`


### Challenge 2 : Long Names
```py
names = ["Alex", "Beth", "Carolina", "Dave", "Freddie"]
long_names = [name.upper() for name in names if len(name) > 5]
```

>[!success]- Output
>`['CAROLINA', 'FREDDIE']`

### Challenge 3 : Data Overlap
Two files file1.txt and file2.txt is given with random numbers in it. And the challenge is to write a piece of code that finds the overlapping values and adds it to a list.
```file1.txt
3
6
5
8
33
12
7
4
72
2
42
13
```

```file2.txt
3
6
13
5
7
89
12
3
33
34
1
344
42
```

The challenge was to accomplish this without a conventional for loop but with the List Comprehension method.

```py
with open("file1.txt") as f:
  lines1 = f.readlines()
lines1 = [line.strip() for line in lines1]
lines1 = [int(line) for line in lines1]

with open("file2.txt") as f:
  lines2 = f.readlines()
lines2 = [line.strip() for line in lines2]
lines2 = [int(line) for line in lines2]

result = [num for num in lines1 if num in lines2]


# Write your code above 👆
print(result)
```

## Dictionary Comprehension
We can iterate through a dictionary the same way we do with the list.
```py
new_dict = {new_key:new_value for item in list}
```

If we are to iterate through another dictionary, we should use the syntax
```py
new_dict = {new_key:new_value for (key:value) in dictionary.items() if ...}
```
### Challenge 4 : Split Sentence
```py
sentence = input()
result = {word:len(word) for word in sentence.split()}
print(result)
```

>[!success]- Output
>`{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}`

## Conventional way of looping through a dictionary
```py
student_dict = {
	"student" : ["Angela", "James", "Lily"],
	"score": [56, 76, 98]
}

for (key, value) in student_dict.items():
	print(key)
	print(value)
```

## Looping through a dictionary using Pandas
```
import pandas  
  
  
student_dict = {  
    "student": ["Angela", "James", "Lily"],  
    "score": [56, 76, 98]  
}  
  
student_dataframe = pandas.DataFrame(student_dict)  
print(student_dataframe)

# Loop through a dataframe
for (key, value) in student_dataframe.items():
	print(value)

# Loop through rows of data using Pandas
for (index, row) in student_dataframe.iterrows():
	print(row)
	print(row.student)
	print(row.score)

```
