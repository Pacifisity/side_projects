"""
You are a grade school teacher who wants to make a randomized multiplication quiz for your students.
You will use programming to make the quiz, which is to consist of ten questions, each the multiplication of two random integers between 0 and 12.
The program will write the quiz to a text file called myMultiplicationQuiz.txt which will be in the format below (note only the first three questions are shown).
Your program needs to import the random module and use its randint function.  The program should use a loop to efficiently write all ten problems.

    1) 3 x 12 = _____
    2) 5 x 6 = _____
    3) 0 x 7 = _____
"""
import random

# The questions function takes in our input and molds it into randomly generated questions
def questions(number):
    question_count = 0
    questions = []
    while question_count < number:
        n1 = random.randint(1,12); n2 = random.randint(1,12)
        questions.append(f"{question_count + 1}) {n1} * {n2} = __________")
        question_count += 1
    return (questions)

number = int(input('How many questions?\n'))
f = open(".\math_test.txt", 'w')

# This for loop is taking the returned list and iterating through each item and writing it into the text file
for question in questions(number):
    f.write(f"{question}\n")
f.close()
