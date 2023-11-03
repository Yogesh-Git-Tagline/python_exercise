"""You are given a list of email addresses. Filter out the validate emails."""

import re  # importing the re module to implement regular expression

# defining what should be include in email using re.compile() method referd as symbols
symbols = re.compile(r'([A-Za-z0-9_-])+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,3})')

# method for check the comming mail as parameter is valid or not
def CheckValid(email):
    # isValid is filter out the correct email
    isValid = re.fullmatch(symbols, email)
    if isValid:
        return True  # if any correct email is found then function will satisfied and return true
    else:
        return False  # if all email is found as invalid then function will return false


validEmail = []  # list for store valid emails from given list of emails

# given list of emails
emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space', 'no-reply@domain.in',
          'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123', 'fake@fake123.fakercom', 'ypc123@gmai.com']

# below loop is iterate over emails-list and pass each email as an argument in CheckValid fun
for i in emails:
    if CheckValid(i):
        validEmail.append(i)  # valid emails is adding in validEmail list

print(validEmail)  # finally we can see the list of filtered email address.
