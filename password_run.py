
__Author__ = "Mouza Alameri"
__Date__ = "13/05/2025"

#using generators to find weak passwords 

import string 

def displaymsg(): 
    print("Hello, this program will find the weak passwords from a list of passwords and anything less then 8 or has no character will b labled as weak")
    print("otherwise it would be labeled as strong ")

displaymsg()

passwordz = [
    "12345678",              # weak
    "qwerty123",             # weak
    "HomeSweetHome2025!",    # strong
    "iloveyou",              # weak
    "G@mer_G1rl_88",         # strong
    "admin",                 # very weak
    "LetMeIn!!",             # medium
    "password",              # worst
    "WiFi4Life#2024",        # strong
    "xXx_Hack3rGod_xXx",     # strong
    "mypass",                # weak
    "MouzaRul3s!",           # strong 
    "guest1234",             # common/weak
    "R@spberryPi!",          # strong
    "secret",                # weak
    "Dubai$unset2025",       # strong
]



def find_weak(pwd_list):
    special_chars = set(string.punctuation)  # define once before the loop
    for pwd in pwd_list:
        has_special = any(char in special_chars for char in pwd)
        if len(pwd) < 8 or not has_special:
            yield pwd

 
    print(" Weak Passwords:")
for weak in find_weak(passwordz): 
    print("WEAK", weak)
print()


for pwd in passwordz:
    print("Preview:", pwd[:3] + "***")                      #this part is done to integrate the use of string slicing as learnt before 


def goodbye():
    print("Thank you for trying out the program ! ")
goodbye()