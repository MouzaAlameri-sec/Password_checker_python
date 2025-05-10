
__Author__ = "Mouza Alameri"
__Date__ = "10/05/2025"

# passwprdchecker using OOP [encapsulation]
# PT2 of Password_check_Python

import string
import math
import hashlib
import requests
from colorama import Fore, Style, init

init()
pwd = input("Enter password: ")
redflagz = []

class PasswordStrengthChecker: 
    def __init__(self, passwrd):
        self.pwd = passwrd

    def length_check(self): 
        if len(self.pwd) < 6: 
            print(Fore.RED + "Weak in length — strengthen by adding more values" + Style.RESET_ALL)
        elif len(self.pwd) <= 10: 
            print(Fore.YELLOW + "Mid — add more length for password to be strong" + Style.RESET_ALL)
        elif any(char.isdigit() for char in self.pwd) or any(not char.isalnum() for char in self.pwd):
            print(Fore.GREEN + "Strong password" + Style.RESET_ALL)
        else:
            print("Decent password")

    def symbols_check(self):
        if not any(char in string.punctuation for char in self.pwd):
            redflagz.append("Missing a symbol (e.g., @, #, !, etc.)")

    def uppercase(self):
        if not any(char.isupper() for char in self.pwd):
            redflagz.append("Missing an uppercase letter")
    
    def digit(self):
        if not any(char.isdigit() for char in self.pwd):
            redflagz.append("Missing a number")
    
    def evaluate_results(self):
        if not redflagz: 
            print(Fore.CYAN + "Congrats! Your password is somewhat secure!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "\nPassword issues found:" + Style.RESET_ALL)
            for issue in redflagz:
                print("* " + issue)
            print("Please try again :)")

    def check_breach(self):
        sha1 = hashlib.sha1(self.pwd.encode()).hexdigest().upper()
        prefix = sha1[:5]
        suffix = sha1[5:]

        response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
        if response.status_code != 200:
            print("Error contacting breach API.")
            return

        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                print(Fore.RED + f"\n  This password was found in a data breach {count} times!" + Style.RESET_ALL)
                return
        print(Fore.GREEN + "\n Password not found in known breaches." + Style.RESET_ALL)

    def estimate_entropy(self):
        charset = 0
        if any(c.islower() for c in self.pwd): charset += 26
        if any(c.isupper() for c in self.pwd): charset += 26
        if any(c.isdigit() for c in self.pwd): charset += 10
        if any(c in string.punctuation for c in self.pwd): charset += 32

        entropy = math.log2(charset) * len(self.pwd)
        print(Fore.MAGENTA + f"\nEstimated entropy: {round(entropy, 2)} bits" + Style.RESET_ALL)

        attempts_per_second = 1e9
        seconds = 2 ** entropy / attempts_per_second
        quantum_seconds = 2 ** (entropy / 2) / attempts_per_second

        print("Estimated brute-force time:", format_time(seconds))
        print("Quantum brute-force time (estimated):", format_time(quantum_seconds))

def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} days"
    years = days / 365
    return f"{years:.2f} years"

checker = PasswordStrengthChecker(pwd)
checker.length_check()
checker.symbols_check()
checker.uppercase()
checker.digit()
checker.evaluate_results()
checker.check_breach()
checker.estimate_entropy()

def goodbyemsg(): 
    print("\nThank you for trying this out!")

goodbyemsg()
