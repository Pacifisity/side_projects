# You are a runner who wants to write a program to keep track of daily miles run.
# Your program uses a for loop to loop through each day in a week, prompting the user to input the number of miles run on that day.
# The program stores these seven numbers in a list, initializing the list as empty, and using the append() method to append to it.
# After the loop, the program uses the sort() method to display the sorted list.
# For example:
#        Enter the number of miles run on Sunday: 5
#        Enter the number of miles run on Monday: 3
#        Enter the number of miles run on Tuesday: 13.1
#        Enter the number of miles run on Wednesday: 10
#        Enter the number of miles run on Thursday: 0
#        Enter the number of miles run on Friday: 20
#        Enter the number of miles run on Saturday: 6.2
#        The sorted number of daily miles is: 
#
#        [0, 3, 5, 6.2, 10, 13.1, 20]

miles_ran = [] # initializes the list, we need this to add more to the list later
days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] # Creating a list with all the week days so we can use it for our 'for' statement
iteration = 0 # This is a placeholder variable that we use to select each item in the list, we use it to tell the program which item we want
for day in days_of_the_week: # for loop with each item in 'days_of_the_week being' defined as 'day'
    miles_input = float(input("Enter the number of miles you've ran on " + days_of_the_week[iteration] + ': ')) # input variable that holds the miles ran, this will later be added to our initialized list
    if miles_input % 1 == 0: # if statement that used the % syntax to find the remainder, this statement checks if there is no remainder and if there isn't it turns it into an integer
        miles_input = int(miles_input) # basic variable type conversion
    miles_ran.append(miles_input) # This uses the append method, append adds a variable's value into a list; in this case 'miles input'
    iteration += 1 # adds one to our placeholder variable
miles_ran.sort() # Uses the sort method to sort the variable from lowest to highest
print(miles_ran) # prints your list