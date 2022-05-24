"""
You are a student who wants to write a program to manage your class schedule.  Each course you take has a name and a number of credits, so arranging this information is perfect for a dictionary.  Write a program that prints each course name followed by its number of credits.  To do this, write a function that accepts a dictionary as input and then employs a for loop to loop through each key-value pair in your dictionary, printing along the way.  The main program should call your function with the following dictionary:

        {'ENGR120-Programming For Engineers': 2, 'ENGR290-Circuit Analysis': 3, 'MATH212-Differential Equations': 4, 'ENGL103-Freshman English II for Engineers': 3},

which would be printed as

        ENGR120-Programming For Engineers: 2 credits

        ENGR290-Circuit Analysis: 3 credits

        MATH212-Differential Equations: 4 credits

        ENGL103-Freshman English II for Engineers: 3 credits
"""
def display_classes(course_information):
    print('Class Schedule:')

    for key, amount in course_information.items():
        print(' ' + key + ': ' + str(amount), ' Credits')

course_information = {'ENGR120-Programming For Engineers': 2, 'ENGR290-Circuit Analysis': 3, 'MATH212-Differential Equations': 4, 'ENGL103-Freshman English II for Engineers': 3}
display_classes(course_information)