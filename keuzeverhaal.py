from multiprocessing.connection import wait
import random
import time

# Possible answers
items: list = ["Schroevendraaier", "EHBO doos", "4 blikken voedsel", "Warme kleren"]

look: list = ["Kijk", "kijk", "K", "k"]
use: list = ["Gebruik", "gebruik", "G", "g"]
move: list = ["Move", "move", "M", "m"]

# Items
inventory: list = []

# Misc
player_name: str


# Pick items
def pick_items():
    global inventory

    print("Keuzes: Schroevendraaier, EHBO doos, 4 blikken voedsel, Warme kleren")

    choosing: bool = True
    times: int  = 2
    while choosing:
        picked_item: str = input("Keuze: ")

        match picked_item:
            case "Schroevendraaier":
                print("Je hebt nu een schroevendraaier.")
                inventory.append("Schroevendraaier")
            case "EHBO doos":
                print("Je hebt nu een EHBO doos.")
                inventory.append("EHBO doos")
            case "4 blikken voedsel":
                print("Je hebt nu 4 blikken eten.")
                inventory.append("4 blikken voedsel")
            case "Warme kleren":
                print("Je hebt nu warme kleding")
                inventory.append("Warme kleren")
        
        if picked_item not in items:
            print("Sorry, dat ligt er niet.")
        else: 
            times -= 1
        
        if times <= 0:
            print("Nu je je spullen hebt is het tijd om te vertrekken.")
            choosing = False



# Start
def prologue():
    global player_name

    # Get player name
    name = input("Wat is je naam? ")
    player_name = name
    time.sleep(0.5)

    # Intro
    print("Het is 2010. In het land Oerand heerst een hevige oorlog om olie. Het is een nutteloze oorlog die vele levens claimt en gezinnen uit elkaar trekt. ")
    print("Mensen proberen te vluchter maar worden getroffen door mensen handel ")
    print("en de wereld van drugs...")

    time.sleep(3)

    print("Jij bent een tiener, genaamd", str(name) + ".")
    print("Je bent van plan om te ontsnappen uit Oerand en asiel te zoeken in Heeland, een Westers land met genoeg kansen. Je zit op dit moment thuis, ")
    print("je ouders zijn een tijd geleden spoorloos verdwenen. Er valt een lichte straal van elegant licht naar binnen en er ")
    print("dwarrelen allemaal stof deeltjes door de lucht. Er liggen een aantal objecten in het huis. ")
    print("Je besluit er een aantal mee te nemen in je rugzak voor je gaat.")

    time.sleep(5)

    pick_items()

    print("Vannacht gaat er een groepje uit je dorp via de jungle naar het strand om de boot te nemen om te ontsnappen. Je besluit om mee te gaan vanavond.")

    time.sleep(2)

    print("Het is nu 21:00 en het is tijd om te gaan.")



prologue() # Start game