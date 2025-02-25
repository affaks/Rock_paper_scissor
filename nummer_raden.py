import os, platform
import random 

def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
        

geheim_getal = random.randint(1, 100)
pogingen = 0
    
print()
print("Welkom bij het spel Nummer raden! Ik heb een getal tussen 1 en 100 gekozen.")
input("druk op enter om te starten!")
clear()
    
while True:
    gok = input("Raad het getal: ")
        
    if gok.isdigit():
        gok = int(gok)
        pogingen += 1
        clear()
        print(f"Dit is poging nummer: {pogingen}")
            
        if gok < geheim_getal:
            print("het getal is hoger.")
            print()
        elif gok > geheim_getal:
            print("het getal is lager.")
            print()
        else:
            print(f"CORRECT!!! je hebt het juiste getal {geheim_getal} geraden in {pogingen} pogingen!")
            break
    else:
        print("voer een getal in!")



    