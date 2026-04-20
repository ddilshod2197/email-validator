import re

def email_formati(email):
    shartlar = [
        re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email) is not None,
        len(email) <= 254,
        email.count('@') == 1,
        email[0] != '@',
        email[-1] != '@'
    ]

    return all(shartlar)

email = input("Email kiriting: ")
print(email_formati(email))
