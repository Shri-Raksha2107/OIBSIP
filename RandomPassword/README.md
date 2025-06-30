Random Password Generator

This Python code generates a secure random password based on user-selected criteria such as letters, digits, and special characters.

Objective

To create a password generator that lets users customize the characters used, ensuring a mix of security and flexibility for creating strong passwords.

Features

-Users can choose any combination of:

-Letters (uppercase & lowercase)

-Digits

-Special characters

-User-defined password length

-Input validation and simple UI via terminal.

-Randomized password output.

Tools Used

-Python 

-random module

-string module for character sets.

How it works

-User inputs the desired password length

-Chooses which types of characters to include:

-Letters (string.ascii_letters)

-Digits (string.digits)

-Special characters (string.punctuation)

-After entering their choices, they must enter 4 to exit the selection loop.

-The program randomly selects characters from the chosen pool and prints the password.

Sample Output

Enter the length of the password: 10

What kind of random password you want? 

 1.Letters 
 
 2.Digits 
 
 3.Special Characters 
 
 4.Exit

Enter your choice: 1

Enter your choice: 2

Enter your choice: 4

Your Random password is: x9PqA7dYtB

Outcome

-A customizable and secure password generator

-Great for understanding loops, conditionals, and string manipulation in Python






