import random
#import system
import os
def say(something):
    from os import system
    print("%s" % something)
    system('say "%s"' % something)
    
 
guessesTaken = 0

myName=input('Hello! Cual es tu nombre?')
 #= input()

number = random.randint(1, 20)
say('Bien, ' + myName + ', Estoy pensando un numero entre 1 y 20. (Presiona "q" para salir)')
seguir=1
while seguir==1 :
      
    say('Adivina.') # There are four spaces in front of print.
    guess1 = input()
    if guess1=="q":
        number = str(number)
        say(':( Perdiste. El numero era: ' + number)
        break

    guess = int(guess1)

    guessesTaken = guessesTaken + 1

    if guess < number:
        say('Has dicho un numero menor.') # There are eight spaces in front of print.

    if guess > number:
        say('Has dicho un numero mayor.')

    
    if guess == number:
        guessesTaken = str(guessesTaken)
        say('SUPER, ' + myName + '! Lo has adivinado en  ' + guessesTaken + ' intentos!')
        
        var1=input("\nQuieres seguir Si o No?")
        if var1=="s" or var1=="S":
            seguir=1
            try:
                os.system('clear')
                number = random.randint(1, 20)
                guessesTaken=0
                say('Ya pense otro numero entre 1 y 20')
            except:
                os.system('cls')  
        
        else:
            seguir=2

   

    