__author__ = "Mouza Alameri"
__date__ = "30/04/2025" 

print("Welcome to the password strength checker <3")

import string

while True:
    pwd = input("Enter the password that you want to be checked: ")
    redflagz = []

    # Check password length
    if len(pwd) < 8: 
        redflagz.append("Too bad this is too short :( Fix: 8 characters or more")
    
    # Check for digits
    if not any(char.isdigit() for char in pwd):
        redflagz.append("Missing a digit from 0-9")
    
    # Check for uppercase letters
    if not any(char.isupper() for char in pwd):
        redflagz.append("Missing an uppercase letter")
    
    # Check for symbols
    if not any(char in string.punctuation for char in pwd):
        redflagz.append("Missing a symbol (e.g., @, #, !, etc.)")

    # Evaluate results
    if not redflagz: 
        print("Congrats! Your password is somewhat secure!")
        break
    else:
        print("Password issues found:")
        for issue in redflagz:
            print("* " + issue)
        print("Please try again :)")

print("Thanks for checking your password strength!")