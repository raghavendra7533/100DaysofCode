name = "Raghav"
names_of_employees = {
    "John": "Junior Manager",
    "Sameer": "Senior Manager",
    "Sunil": "Head of Training"
}


with open("email_template.txt") as letter:
    content = letter.read()
    for i in names_of_employees:
        new_letter = content.replace("[NAME]", i)
        new_letter = new_letter.replace("[DESIGNATION]", names_of_employees[i])
        new_letter = new_letter.replace("[YOUR NAME]", name)
        with open(f"Emails/email_{i}.txt", "w") as email:
            email.write(new_letter)
