import time
import random

def register():
    username = str(input("Username: "))
    secure = False
    upper = False; lower = False; alnum = False; strength = 0
    loop_amount = 0

    while not secure:
        password = str(input("Password: "))
        if password == 'Password123':
            print("He has broken the system, we must restrain him...")
            time.sleep(3)
            while loop_amount < 333:
                print(random.randint(1,1e+199))
                loop_amount += 1
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
            print('Alright, hope you can remember that.')
            secure = True
        elif strength > 2:
            strength = 'good'
            print("That's a decent password atleast.")
            secure = True
        elif strength > 1:
            strength = 'weak'
            print("I guess that will work.")
            secure = True    
        else:
            print(f'My grandmother is stronger than your password, {username}')
    print(f'Thank you for registering with a {strength} password, {username}')

attempt = 0

print('Welcome to the dark web.')
time.sleep(1)
while True:
    web_password_input = input('What is the password?:\n')
    attempt += 1
    if web_password_input == 'Password123':
        print('Please register your dark account.')
        time.sleep(1)
        register()
        time.sleep(1)
        print('porn.exe\n')
        print('Credits:\nProgrammer: Pacifisty#5587\nInspiration: Fungi#6187')
        break
    elif attempt >= 2:
        print("Three strikes you're out\nI've had enough of your shit")
        time.sleep(3)
        while True:
            print(random.randint(1,1e+199))
    else:
        print('Wrong.\nWhatever, just call larry...')
        larry_check = input('Do you want to call larry? (yes/no):\n')
        if str.lower(larry_check) == 'yes':
            print('Larry:\nThe password is "Password123"')
