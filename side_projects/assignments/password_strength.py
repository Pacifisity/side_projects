"""This assignment will have you measure the strength of a password.  Write a program that prompts the user for a password and then prints 'strong', 'good', or 'weak' according to the following rules:

The password is considered strong if it has more than five characeters, and contains at least one upper-case letter, one lower-case letter, and one character that is not alphanumeric.

The password is considered good if it meets all of the strong criteria except it does not contain any non-alphanumeric characters.

The password is considered weak if it meets all of the good criteria except it does not contain any upper-case letters.

Otherwise, the program says the password does not meet minimum security requirements and re-prompts the user to enter a password.  It does this in a loop until the password is at least considered weak.

The program should use the len function as well as the isupper(), islower(), and isalnum() methods."""
username = str(input("Username: "))
secure = False
upper = False; lower = False; alnum = False; strength = 0

while not secure:
    password = str(input("Password: "))
    for character in password:
        if character.isupper():
            upper = 1
        if character.islower():
            lower = 1
        if not character.isalnum():
            alnum = 1
    if len(password) > 5:
        strength += 1
    if upper > 0:
        strength += 1
    if lower > 0:
        strength += 1
    if alnum > 0:
        strength += 1
    if strength > 3:
        strength = 'strong'
        secure = True
    elif strength > 2:
        strength = 'good'
        secure = True
    elif strength > 1:
        strength = 'weak'
        secure = True    
    else:
        print(f'My grandmother is stronger than your password, {username}')
print(f'Thank you for registering with a {strength} password, {username}')

cringe = 'Cringey lord %, %' %('val434ue','valu3434e')