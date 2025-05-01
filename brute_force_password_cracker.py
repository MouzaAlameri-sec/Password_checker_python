__Author__="Mouza Alameri"
print("pls stick to 3-7 length / no symbols/ no captial letters")
print("for anything complex or longer then 3 letter/numb it will take a huge amount of time ")
target = input("Enter a short password (letters/numbers only)(you CAN mix letters and numbers): ")

# 1. Length checkab
if len(target) > 7 or len(target) < 3:
    print(" Pls stick to a password that's 3 to 7 characters long.")

# 2. Capital letter check
if any(char.isupper() for char in target):
    print("pls use only lowercase letters — no CAPITALS allowed.")

# 3. Symbol check
if not all(char.isalnum() for char in target):
    print(" No symbols or spaces allowed. Use only letters and numbers.")

from itertools import product
import time

def mouza_brute_force(targ_pass, allowed_set, max_length):
    start_time = time.time()  # Track start time
    attempts = 0
    
    for length in range(1, max_length + 1):  # Try all lengths up to max_length
        for user_attempt in product(allowed_set, repeat=length):
            attempts += 1
            user_attempt_str = ''.join(user_attempt)
            if user_attempt_str == targ_pass:
                end_time = time.time()
                duration = end_time - start_time
                print(f" Password brute forced in {attempts} attempts!")
                print(f"Time taken: {round(duration, 2)} seconds")
                return user_attempt_str
    return None  # Only return None after all attempts

allowed_set = "abcdefghijklmnopqrstuvwxyz0123456789"
print(f"brute forcing ur passwrd...")

found = mouza_brute_force(target, allowed_set, max_length=7)
print(f"Password cracked: {found}")