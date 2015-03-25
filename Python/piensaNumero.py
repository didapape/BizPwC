#import system
import random
import os
def say(something):
    from os import system
    print("%s" % something)
    system('say "%s"' % something)
    
    
def adivinar():
    try:
        os.system('clear')
    except:
        os.system('cls')
        
    var1=input ("piensa un numero...")
    var2=input("multiplicalo por 2")
    sumado= random.randint(10, 50)
    if sumado%2 >0 :
        sumado=sumado*2;
        
    var3=input ("sumale "+ str(sumado) +"...")
    var4=input("El resultado dividelo por la mitad")
    var5=input("Restale el numero que has pensado...")
    say("ahora lo adivinare....")
    var1=input()
    say('....Dejame pensar....')
    var3=input()
    varTotal="..El resultado es " + str(int(sumado/2))
    say(varTotal)

	
seguir=1
while seguir:
    adivinar()
    
    volver=input("\n..Volver a jugar S o N?")

    if volver=="S" or volver=="s":
        seguir=1
    else:
    	seguir=0
    	print("bueno bye bye....")
