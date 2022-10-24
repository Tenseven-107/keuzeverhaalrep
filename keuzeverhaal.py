from multiprocessing.connection import wait
import random
import time
import os

# Door Noah Adrichem, SD1C

# Possible answers
items: list = ["Schroevendraaier", "EHBO doos", "4 blikken voedsel", "Warme kleren"]

look: list = ["Kijk", "kijk", "K", "k"]
use: list = ["Gebruik", "gebruik", "G", "g"]
move: list = ["Beweeg", "beweeg", "B", "b"]

yes: list = ["Ja", "ja", "J", "j"]
no: list = ["Nee", "nee", "N", "n"]

# Items
inventory: list = []

# Misc
player_name: str
player_moral: int = 100



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



# Game over
def game_over():
    global player_moral

    os.system("cls")
    print("Game over! Je moraal was", str(player_moral), "punten!")



# Chapter 1
def chapter_1():
    global inventory
    global player_name
    global player_moral
    global yes
    global no

    print("???: Wordt wakker slaapkop!")
    time.sleep(2)
    print("Ik zei, wordt wakker, idioot!")
    time.sleep(1)
    print("Je voelt een tik, en wordt meteen wakker..")

    time.sleep(5)
    print("???: Mooi, je bent wakker.")
    print("Je kijkt om je heen en ziet dat er mensen van de boot afstappen.")
    print("De man naast staat die je wakker maakte staat nu rondt te zwaaien.")
    print("Hij heeft een AK-47 in zijn hand en ziet er gestrest uit.")
    print("Hij draagt een wit overhemd en een vieze spijkerbroek.")

    time.sleep(10)

    print("Je besluit om op te staan.")

    wc1 = False
    while wc1 == False:
        qp1 = input("Wat wil je doen? ")
        if qp1 in look:
            print("Het licht in de openlucht waar je staat is licht. ")
            print("Je ziet allemaal mensen van de boot vertrekken.")
        elif qp1 in use:
            if "Kettinkje" not in inventory:
                print("Je ziet een kettinkje liggen op de grond. Oppakken?")

                qp2 = input()
                if qp2 in yes:
                    print("Je pakt het op en stopt het in je rugzak.")
                    print("Je hebt nu een kettinkje. Het bevat een blauwkleurige steen")
                    print("en is voor de rest zilver.")

                    inventory.append("Kettinkje")
                elif qp2 in no:
                    print("Je laat het liggen")

            else:
                print("Er is niks.")

        elif qp1 in move:
            print("Je pakt je rugzak op en vertrekt van de boot af.")
            wc1 = True




# Start
def prologue():
    global player_name
    global player_moral
    global yes
    global no

    player_moral = 100

    # Get player name
    name = input("Wat is je naam? ")
    player_name = name
    time.sleep(0.5)

    # Intro
    print("Het is 2010. In het land Oerand heerst een hevige oorlog om olie. Het is een nutteloze oorlog die vele levens claimt en gezinnen uit elkaar trekt. ")
    print("Mensen proberen te vluchter maar worden getroffen door mensen handel ")
    print("en de wereld van drugs...")

    time.sleep(10)

    print("Jij bent een tiener, genaamd", str(name) + ".")
    print("Je bent van plan om te ontsnappen uit Oerand en asiel te zoeken in Heeland, een Westers land met genoeg kansen. Je zit op dit moment thuis, ")
    print("je ouders zijn een tijd geleden spoorloos verdwenen. Er valt een lichte straal van elegant licht naar binnen en er ")
    print("dwarrelen allemaal stof deeltjes door de lucht. Er liggen een aantal objecten in het huis. ")
    print("Je besluit er een aantal mee te nemen in je rugzak voor je gaat.")

    time.sleep(15)

    pick_items()

    print("Vannacht gaat er een groepje uit je dorp via de jungle naar het strand om de boot te nemen om te ontsnappen. Je besluit om mee te gaan vanavond.")

    time.sleep(5)

    print("Het is nu 21:00 en het is tijd om te gaan.")

    time.sleep(2)

    print("Je staat buiten, Wat wil je doen?")
    print("(In dit verhaal kun je drie antwoorden gebruiken, [Kijk], [Gebruik] en [Beweeg].)")

    wc1 = False
    while wc1 == False:
        qp1 = input("Wat wil je doen? ")
        if qp1 in look:
            print("Het is buiten donker, en het dorp ziet er verlaten uit. Je staat bij de deur")
            print("en over je heen straalt goud-kleurig lamplicht dat meerdere motten aantrekt.")
            print("Voor je is een pad de jungle in.")
        elif qp1 in use:
            print("Er is niks om te gebruiken.")
        elif qp1 in move:
            print("Je beloopt het pad de jungle in. Na een tijdje kom je aan bij de groep mede-vluchtelingen uit het dorp.")
            wc1 = True
    
    print("Dorpeling A: We moeten gaan! De boot vertrekt over tien minuten!")
    print("Dorpeling B: *fluisterend* Is iedereen er?")

    qp2 = input()
    if qp2 in yes:
        print("Dorpeling A: Dan is het tijd om te gaan.")
    elif qp2 in no:
        print("Dorpeling B: We moeten nu echt gaan!!")
        player_moral -= 1
    
    print("Je loopt het pad af samen met de groep. Je komt na een tijdje van snel lopen ")
    print("In een snel tempo aan bij een riviertje.")

    time.sleep(2)

    print("Opeens zie je allemaal lichten in de schemering om je heen verschijnen uit de bosjes. Één van de dorpelingen begint te schreeuwen.")
    print("Dorpeling C: Ze hebben ons gevonden!! Rennen!")

    wc2 = False
    while wc2 == False:
        qp3 = input("Wat ga je doen?! ")
        if qp3 in look:
            print("Je ziet overal zaklampen om je heen. Een aantal soldaten komen akelig dichtbij, maar hebben je nog niet gezien.")
            player_moral -= 1
        elif qp3 in use:
            print("Je verstopt jezelf. Nadat de soldaten weg zijn steek je stiekem de rivier over.")
            wc2 = True
        elif qp3 in move:
            print("Je probeert te rennen maar wordt gespot zodra je de rivier over probeert te steken.")
            print("Je voelt een klap tegen je kop en wordt wakker. JE BENT GEVANGEN GENOMEN DOOR DE CORRUPTE SOLDATEN VAN OERAND [Einde 1 van de 4]")
            print("Wil je nog een keer?")
            cp1 = input()
            if cp1 in yes:
                prologue()
            elif cp1 in no:
                game_over()
                break
 
    time.sleep(2)

    print("Je weet waar het strand is. Je rent naar het strand toe zo snel mogelijk en komt bij de boot.")
    print("Achter je hoor je schoten, maar het enigste waar je momenteel aan kunt denken is vluchten.")

    time.sleep(5)

    print("Bij de boot kom je een aantal dorpelingen tegen.")
    print("Dorpeling B: Snel! we hebben niet veel tijd meer", player_name + ".")

    time.sleep(5)

    print("Je stapt op de boot met ongeveer de helft van de groep waarmee jullie eerst waren.")
    print("Je Loopt over het dek terwijl de boot geduwd wordt de zee in. Langzaam zie je de wal verdwijnen.")
    print("Op de boot zitten huilende moeders, kinderen zonder ouders en gewonden.")
    print("Je zoekt een plek op waar je plaats kan nemen en sluit je ogen, je wilt nooit meer deze avond herinneren.")

    time.sleep(25)

    end_q = input("Wil je nu verder?:")
    if end_q in yes:
        os.system("cls")
        chapter_1()



prologue() # Start game