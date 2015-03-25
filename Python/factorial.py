from os import system

#this say function is the most important part of kids programming
#it uses the built in OSX say command to convert text to speech
def say(something):
    system('say "%s"' % something)

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
        
first_line = "Type the number you want to do a factorial for."
print(first_line)
say(first_line)
number = input('?')
answer = factorial(number)
answer_string = "The answer is %d" % answer
print(answer_string)
say(answer_string)
