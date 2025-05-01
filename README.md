# Brute_Force_Python

This code brute-forces a password that a user enters with a maximum length of 7. It performs user input validation and returns the number of attempts and the duration of how long it took to brute-force/crack the password.

---

## Table of Contents
- [Overview](#overview)
- [Errors and Fixes](#errors-and-fixes)
- [Code Limitations](#code-limitations)
- [Future Improvements](#future-improvements)

---

## Overview

The original code had several errors that were resolved through careful debugging and trial-and-error. The final version successfully brute-forces passwords while validating user input against specific criteria.

---

## Errors and Fixes

1. **Error Display Timing:**
   - **Original Issue:** Conditions for input validation were displayed after the user entered the password.
   - **Fix:** Moved the print statement above the input statement to display validation rules first.

2. **Variable Name Mismatch:**
   - **Original Issue:** The charset was defined as `charset` but referenced as `allowed_set` in the function.
   - **Fix:** Renamed the variable consistently throughout the code.

3. **Undefined `start_time`:**
   - **Original Issue:** The variable `start_time` was used without being defined.
   - **Fix:** Added `start_time = time.time()` at the beginning of the brute-force function.

4. **Typo in `char.isalnum()`:**
   - **Original Issue:** A typo (`char.issum`) caused a syntax error.
   - **Fix:** Corrected the method name to `char.isalnum()`.

5. **Indentation Error:**
   - **Original Issue:** The `return None` statement was incorrectly indented.
   - **Fix:** Adjusted indentation to ensure proper loop execution.

6. **Tracking Attempts:**
   - **Original Issue:** The code did not track the number of attempts made.
   - **Fix:** Added an `attempts` variable to count each password guess.

---

## Code Limitations

- **Performance with Longer Passwords:**
  - Cracking passwords of 6-7 characters takes significantly longer due to the exponential increase in possible combinations.
  - This limitation is inherent to brute-force attacks and cannot be easily mitigated.

- **Input Validation:**
  - The program does not exit automatically if the user enters invalid input (e.g., passwords outside the 3-7 character range or containing invalid characters).
  - It attempts to brute-force the password despite validation failures.

- **Scope of Validation:**
  - The code checks for lowercase letters and numbers but does not account for uppercase letters, punctuation, or symbols.

---

## Future Improvements

- **Automated Exit on Validation Failure:**
  - Implement an exit function to stop the program immediately if input validation fails.

- **Alternative Attack Methods:**
  - Explore different password-cracking techniques (e.g., dictionary attacks) for better performance.

- **Enhanced Validation:**
  - Expand input validation to include checks for uppercase letters, punctuation, and symbols.

- **Progress Tracking:**
  - Add real-time feedback on the brute-force progress (e.g., percentage completed).

---

## Final Thoughts

I'm very proud of this code—it represents a significant milestone in my learning journey. Despite its limitations, it demonstrates a solid understanding of brute-force concepts and Python scripting. This project has been an invaluable learning experience, and I look forward to building on these foundations in future projects.
