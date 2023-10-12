import pandas


student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)