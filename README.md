
# Brute_Force_Python
This code brute forces a password that a user enters with a max length of 7. does user validation on whatever the user inputs. and returns attempts and the duration of how long it took to brute force / crack the password 


the original code has alot of errors using kimi ai and trial and error these error were resolved. 

#error 1:

the code displayed the conditions for the error after the user enters the password i changed that by putting the print statement above the input statement 
#error 2 : 

i named charset ="abcdefghijklmnopqrstuvwxyz0123456789" but i defined it as allowed_set in my main function. this happened because i was looking at diff code and i was adjusting this one to my liking 

#error 3:
start_time was not defined 

#error 4: 
typo in char.issum 

#error5 : 
indentation 

3error 6 : 
added attempts 

#limitations of this code and future corrections : 

- for longer passwords from 6-7 letters it starts taking a hugeee amount of time to crack the password and it will remain that way becuase if the way this attack works 
- when the user does make an error in the input the program doesnt exit it still attempts to crack the password
- doesnt take into account captial letters, puncuations and symbols

- all around im very happy and proud of this code its my first code where i do something as dense but it has its own limitations 

for future use I def would add an exit function and attempt a different type of attack overall. 
>>>>>>> 955fe834a5763ae46879f6727c9f2c2ff0826ad4
