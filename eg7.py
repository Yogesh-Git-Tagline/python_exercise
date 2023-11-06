"""You are given a list of email addresses. Filter out the validate emails."""

import re     #importing the re module to implement regular expression

#defining what should be include in email using re.compile() method referd as email_symbols
email_symbols = re.compile(r'([A-Za-z0-9_-])+@[A-Za-z0-9]+(\.[A-Z|a-z]{2,3})')

#method for check the comming mail as parameter is valid or not 
def check_email(email):
    is_valid=re.fullmatch(email_symbols, email)   #is Valid is filter out the correct email 
    if is_valid:
      return True        #if any correct email is found then function will satisfied and return true
    else:
      return False       #if all email is found as invalid then function will return false

valid_emails=[]     #list for store valid emails from given list of emails

#given list of emails
emails = ['abc@gmail.com', '123$tt*@xyz.com', 'good@bad@uk.in', 'nasa@usa12.space', 'no-reply@domain.in', 'ramhanuman@saketa.lok', 'ruhi.mohan@exter123.123', 'fake@fake123.fakercom','ypc123@gmai.com']

#below loop is iterate over emails-list and pass each email as an argument in check_email function
for email in emails:
   if check_email(email):
      valid_emails.append(email)   #valid emails is adding in valid Email list

print(valid_emails)    #finally we can see the list of filtered email address.
