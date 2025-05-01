# Brute_Force_Python
This code brute forces a password that a user enters with a max length of 7. does user validation on whatever the user inputs. and returns attempts and the duration of how long it took to brute force / crack the password 

this is the og code before the final modification : 
__Author__="Mouza Alameri"

target = input("Enter a short password (letters/numbers only)(you CAN mix letters and numbers): ")
print("pls stick to 3-7 length / no symbols/ no captial lettersA")

 # 1. Length check
if len(target) > 7 or len(target) < 3:
    print(" Pls stick to a password that's 3 to 7 characters long.")

# 2. Capital letter check
if any(char.isupper() for char in target):
    print("pls use only lowercase letters — no CAPITALS allowed.")

# 3. Symbol check #the char.isalum is  useful function that checks for puncuations etc 
if not all(char.isalnum() for char in target):
    print(" No symbols or spaces allowed. Use only letters and numbers.")

from itertools import product
#importing product()
#it would basically look at all the possible combinations of letter or numbers with the lengths up to 7 ex:(a,a)(a,b) 
import time #this is used for checking the duration of the attempts 

def mouza_brute_force(targ_pass,allowed_set,max_length):
    for length in range(1,max_length+1): #loops until max length aka 7
        for user_attempt in product(allowed_set, repeat=length):
            user_attempt=''.join(user_attempt)
            if user_attempt == targ_pass:
                end_time = time.time() 
                duration = end_time - start_time
                print(f" Password brute forced in {attempts} attempts!")
                print(f"Time taken: {round(duration, 2)} seconds")
                return user_attempt
            return None 
charset = "abcdefghijklmnopqrstuvwxyz0123456789"
print(f"brute forcing ur passwrd...")

found = mouza_brute_force(target, allowed_set, max_length=7)
print(f"Password cracked: {found}")

as you can see the original code has alot of errors using kimi ai and trial and error these error were resolved. 

error 1: the code displayed the conditions for the error after the user enters the password i changed that by putting the print statement above the input statement 
error 2 : i named charset ="abcdefghijklmnopqrstuvwxyz0123456789" but i defined it as allowed_set in my main function. this happened because i was looking at diff code and i was adjusting this one to my liking 
error 3: start_time was not defined 
error 4: typo in char.issum 
error5 : indentation 
error 6 : added attempts 

limitations of this code and future corrections : 

- for longer passwords from 6-7 letters it starts taking a hugeee amount of time to crack the password and it will remain that way becuase if the way this attack works 
- when the user does make an error in the input the program doesnt exit it still attempts to crack the password
- doesnt take into account captial letters, puncuations and symbols

- all around im very happy and proud of this code its my first code where i do something as dense but it has its own limitations 

for future use I def would add an exit function and attempt a different type of attack overall. 
