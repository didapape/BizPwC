from os import system
from random import randint

#this say function is the most important part of kids programming
#it uses the built in OSX say command to convert text to speech
def say(something):
    system('say "%s"' % something)

#how big a number should we guess? 
max_number = 10
first_line = "Adivina un número entre 1 y %d" % max_number
print(first_line)
say(first_line)
number = randint(1, max_number)
not_solved = True

#keep looping unil we guess correctly
while not_solved:
    answer = input('?')
    you_said = "Tu escribiste %d" % answer
    say(you_said)
    if answer > number:
        say("Lo siento, el número es menor")
    elif answer < number:
        say("Lo siento, el número es mayor")
    else:
        say("Adivinaste!")
        not_solved = False