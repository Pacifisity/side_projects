import keyboard  # using module keyboard
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('q'):  # if key 'q' is pressed 
            print('You Pressed Q!')
        if keyboard.is_pressed('w'):  # if key 'w' is pressed 
            print('You Pressed W!')
        if keyboard.is_pressed('e'):  # if key 'e' is pressed 
            print('You Pressed E!')
        if keyboard.is_pressed('r'):  # if key 'r' is pressed 
            print('You Pressed R!')
        if keyboard.is_pressed('t'):  # if key 't' is pressed 
            print('You Pressed T!')
        if keyboard.is_pressed('y'):  # if key 'y' is pressed 
            print('You Pressed Y!')
        
    except:
        print('What?!')
        break  # if user pressed a key other than the given key the loop will break