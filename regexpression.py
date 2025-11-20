import re

regex = r'^\d{3}-\d{3}-\d{4}$'

while True:
    phone_number = input("Enter your phone number (format: XXX-XXX-XXXX): ")
    
    if re.fullmatch(regex, phone_number):
        print("Valid Phone Number")
        break 
    else:
        print("Invalid Phone Number, Please Try Again!")
