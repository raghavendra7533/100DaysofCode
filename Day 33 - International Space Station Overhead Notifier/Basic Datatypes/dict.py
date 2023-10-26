dictionary = {
    "key": "value",
    "A seasonal fruit": "Banana",
    "fruit": "Banana",
    "vegetable": "Tomato"
}

# Using dict comprehention
new_dict = {
            dict_key: dictionary[dict_key]
            for dict_key in dictionary
            if dictionary[dict_key] == "Banana"
            }
print(new_dict)