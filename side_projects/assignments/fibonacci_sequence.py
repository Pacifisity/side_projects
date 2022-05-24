print("This program will print Fibonacci Sequence.")
term_amount = 10                                         # amount of terms shown
input = 1                                                # console input for the number to start sequence on
term = 2                                                 # placeholder variable for the first 2 printed terms
n1 = input                                               # first term number variable
print(f"Term: 1, Value: {input}")                        # prints term 1
n2 = input                                               # second term number variable
print(f"Term: 2, Value: {input}")                        # prints term 2

while True:
    term_amount = 10                                     # infinite loop
    if input < 0:                                        # checks for negative integer input
        break                                            # end loop
    else:                                                # positive interget input
        for n in range(term_amount - 2):                 # iteration through your range
            print(f"Term: {term + 1} Value: {n1 + n2}")  # print term and value
            if n2 < n1:                                  # check if n2 is less than n1
                n2 = n1 + n2                             # update n2
            else:                                        # if n1 is less than n2
                n1 = n1 + n2                             # update n1
            term += 1                                    # adds 1 to term count
        break                                            # end loop
        