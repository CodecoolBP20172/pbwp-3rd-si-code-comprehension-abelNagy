import random  # imports the random module

guessesTaken = 0  # assign 0 to the variable guessesTaken

print('Hello! What is your name?')  # prints out string in the argument
myName = input()  # declares the variable myName, sets its value to an user input value

number = random.randint(1, 20)  # randomizes an integer between 1 and 20 and assign it to the number variable
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')  # prints out the message with the number variable

while guessesTaken < 6:  # loop. while the guessesTaken variable's value is less then 6, the following indented code block will repeatedly execute
    print('Take a guess.')  # prints out message (string)
    guess = input()  # declares the variable guess, sets its value to an user input value (string)
    guess = int(guess)  # converts guess variable into an integer type (the input() is a string by default)

    guessesTaken += 1  # increases guessesTaken's value by 1

    if guess < number:  # if the value of guess is less then the value of number the following indented block of code will execute
        print('Your guess is too low.')  # prints out a message (string)

    if guess > number:  # if the value of guess is greater then the value of number the following indented block of code will execute
        print('Your guess is too high.')  # prints out a message (sring)

    if guess == number:  # if the value of guess is equal to the value of number the following indented block of code will execute
        break  # breaks, stops the execution of the while loop, execution goes to the following code lines

if guess == number:  # if the value of guess is equal to the value of number the following indented block of code will execute
    guessesTaken = str(guessesTaken)  # converts guessesTaken variable into an integer type
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')  # prints out message and the values of the variables in the argument (everything as string)

if guess != number:  # if the value of guess is not equal to the value of number the following indtented block of code will execute
    number = str(number)  # converts the number variable into a string type
    print('Nope. The number I was thinking of was ' + number)  # prints out a message and a the number variable's value (string)
