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



# --------------------------------------------------------------------------------------


# Chapter 3
def chapter_3():
    global inventory
    global player_name
    global player_moral
    global yes
    global no

    print("Je wordt wakker en hoort allemaal stemmen.")
    print("Je zit in een tent, op een camping bedje.")
    print("Je bent nog een beetje licht in je hoofd. Naast je ligt je tas.")
    print("Jij: Wat is er gebeurd?")

    time.sleep(12)

    print("Je pakt je tas en loopt naar buiten. Je bent in een vluchtelingen kamp.")

    time.sleep(5)

    print("Je besluit om op het terrein rondt te lopen. Je ziet spelende kinderen,")
    print("moeders die zitten te haken en mannen die zitten te gokken. Het staat er allemaal heel zielig bij.")
    print("Achter je breekt een gevecht los, maar je besluit om het te negeren.")

    time.sleep(10)

    print("De hygiene is vreselijk, de tenten zijn vreselijk, de omgeving is vreselijk,")
    print("de stank is vreselijk, het drinkwater is vreselijk, de grond is modderig en vreselijk,")
    print("alles is vreselijk. Je wilt hier weg.")

    time.sleep(10)

    wc1 = False
    while wc1 == False:
        qp1 = input("Wat wil je doen? ")
        if qp1 in look:
            print("Je ziet twee zand paden voor je. Achter je loopt een lang grind pad.")
            wc1 = True
        elif qp1 in use:
            print("De grond is modderig. Er is helemaal niks.")
        elif qp1 in move:
            print("Maakt niet uit waar je heen gaat, je komt toch op hetzelfde uit.")
            






# Chapter 2.1
def chapter_2_1():
    print("Je loopt weer weg.")
    print("Na zo'n 5 minuten komt er een trein aan, precies degene die je nodig hebt.")
    print("Zodra je in de trein zit begint een lange reis. De trein waar je inzit stopt alleen bij bepaalde stations.")
    print("Je rust wat uit in de trein. De coupé zit vol mensen op hun telefoon.")
    print("De trein reist langs allemaal dorpjes. Na een tijdje rijdt je een stad in.")
    print("Veel mensen in strakke pakken stappen in. Je moet opschuiven voor een ander in de trein.")
    print("Na een hele lange tijd kom je eindelijk bij je eindbestemming, een grens.")

    time.sleep(25)

    print("Er loopt een conducteur nu door de coupé waar je in zit die checkt")
    print("of mensen een kaartje hebben. Je probeert een uitweg te zoeken maar dan zie je")
    print("Dat voor je ook een conducteur loopt!")

    time.sleep(10)

    print("Conducteur: Goedemiddag, mag ik uw kaartje zien?")
    print("Je hebt helemaal geen kaartje! Er is geen uitweg mogelijk!")
    print("Conducteur: komt u maar mee.")

    time.sleep(7)

    print("Je loopt achter de conducteur aan en dan wordt je opeens in boeien gezet.")
    print("Door de stress val je flauw..")

    time.sleep(5)

    end_q = input("Wil je nu verder?:")
    if end_q in yes:
        os.system("cls")
        pass #chapter_3()





# Chapter 2.2
def chapter_2_2():
    global inventory
    global player_name
    global player_moral
    global yes
    global no

    print("Na een tijdje komt de trein aan. Je stapt in en verlaat het dorpje in de bergen.")
    print("Je rust wat uit in de trein en na de hele dag met de trein reizen kom je aan bij de grens.")

    time.sleep(7)

    print("Je steekt de weg over, niks houd je meer tegen. Je wordt wakker op een bankje.")
    print("Je bent vlakbij een parkeer plaats.")

    wc1 = False
    while wc1 == False:
        qp1 = input("Wat wil je doen? ")
        if qp1 in look:
            print("Je zit op een bankje aan de oever van een rivier. achter je is een parkeerplaats.")
            print("Het is mooi weer, je voelt een zomer bries.")

            time.sleep(5)

            print("Je merkt dat er achter je een gorep vluchtelingen is, die een bus in stappen.")
            print("Je weet dat het vluchtelingen zijn vanwege de woorden die ze uitspreken.")
        elif qp1 in use:
            print("Je hebt niks nodig en er is ook niks meer nodig..")
        elif qp1 in move:
            print("Je loopt naar de bus toe, en stapt samen met je trouwe rugzak ook in...")
            wc1 = True
    
    time.sleep(7)

    end_q = input("Wil je nu verder?:")
    if end_q in yes:
        os.system("cls")
        pass #chapter_4()







# Chapter 2
def chapter_2():
    global inventory
    global player_name
    global player_moral
    global yes
    global no

    print("Je voelt je slaperig. Je moet een slaapplek zoeken.")
    print("Het is mistig in het dorp. Het dorp is bergachtig en staat vol bomen en huizen,")
    print("de weggetjes slurven langs de bergwand.")

    time.sleep(10)

    print("Je loopt door het dorp en vindt na een tijdje een bankje")
    print("in een park onder een grote boom.")
    print("Je probeert in slaap te vallen, maar het wilt niet lukken.")
    print("Je hebt het koud. Mischien als je warme kleding hebt voel je je warmer?")

    warme_kleren = False
    if "Warme kleren" in inventory:
        qp1 = input("Wil je je warme kleren gebruiken?" )
        if qp1 in yes:
            print("Je trekt je warme kleren aan je voelt je gelijk al een stuk warmer.")
            print("Nu begin je in slaap te vallen.")

            warme_kleren = True
            player_moral += 30
        elif qp1 in no:
            warme_kleren = False
            print("Je besluit om geen warme kleren aan te trekken.")
    else:
        warme_kleren = False
        player_moral -= 25
        print("Je hebt helaas geen schroevendraaier.")
    

    if warme_kleren:
        print("Je slaapt en hebt een droom over dat alles goed zal komen.")
    else:
        print("Met veel moeiten val je in slaap. Het voelt niet fijn maar je slaapt wel.")
    
    time.sleep(10)

    print("Je wordt wakker op het bankje onder de grote boom. Het begint ochtend te worden.")
    print("Er hangt nogsteeds een mist, maar langzaam begint het op te klaren.")
    print("Je begint wakker te worden en op te staan.")

    time.sleep(12)

    print("Je maakt jezelf klaar voor vandaag.")

    wc1 = False
    while wc1 == False:
        qp2 = input("Wat wil je doen? ")
        if qp2 in look:
            print("Je bent in het park. Je staat naast een bankje onder een grote boom.")
            print("Het park is schoon en omringd met lage, stenen muurtjes.")
            print("Het begint op te klaren van de mist en het is mooi weer.")
            print("De zon schijnt prachtig door de reeks bomen en bergen in de verte.")
        elif qp2 in use:
            print("Op de grond liggen takjes en blaadjes, maar niks nuttigs. Er groeit prachtig groen gras.")
        elif qp2 in move:
            print("Je begint je tas weer in te pakken.")

            if warme_kleren:
                print("Je doet de warme kleren uit en doet ze terug in de tas.")
                player_moral += 10
            else:
                print("Je had het vannacht erg koud.")
                player_moral -= 10

            wc1 = True

    time.sleep(5)

    print("Je begint een beetje wakker te worden en besluit door het dorp te wandelen.")
    print("Je merkt dat het dorp erg authentiek is en zeer zuiders met zijn groen en beige bergen")
    print("en fel gekleurde huizen.")

    time.sleep(7)

    print("Je ziet langzamerhand allemaal mensen hun huis uit komen en te werk gaan.")
    print("Bakkerijtjes starten op, mensen nemen de auto, gaan naar het café..")
    print("Alles is kalm en vredig.")

    time.sleep(7)

    print("Uiteindelijk kom je bij het dorpsplein terecht.")

    wc2 = False
    while wc2 == False:
        qp3 = input("Wat wil je doen? ")
        if qp3 in look:
            print("Het is vredig rondt het plein. In het midden is een prachtige fontein")
            print("waar water uit koppen van leeuwen gespuuwd wordt.")
        elif qp3 in use:
            print("Er is een kaart naast de supermarkt op het plein.")
            print("Je ziet dat er een treinstation in de buurt is.")
            wc2 = True
        elif qp3 in move:
            print("Je ziet een supermarkt maar je herrinert jezelf eraan")
            print("dat je niet genoeg geld hebt. Maar, ernaast staat wel een lokale kaart.")
    
    time.sleep(10)

    print("Je ziet dat er een treinstation in het dorp is en besluit ernaar toe te gaan.")
    print("Het is niet ver en na een tijdje kom je aan bij een treinstation.")
    print("Op het treinstation zie je dat je een kaartje kunt kopen.")
    print("Het is mogelijk om een kaartje te kopen met cash. Mischien heb je geld?")

    if "Geld" in inventory:
        qp1 = input("Wil je een treinkaartje kopen?" )
        if qp1 in yes:
            print("Je pakt het geld uit je tas en geeft hem aan de cashierre.")
            print("Alle taallessen hebben je goed hierop voorbereid.")
            print("Jij: Één treinkaartje graag!")
            print("Cashierre: Alstublieft, nog iets anders?")
            print("Jij: Nee dank je, fijne dag nog!")
            print("Cashierre: Hetzelfde!")

            inventory.append("Treinkaartje")
            inventory.remove("Geld")
            player_moral += 50

            chapter_2_2()
        elif qp1 in no:
            print("Je besluit om geen treinkaartje te kopen.")
            chapter_2_1()
    else:
        print("Maar helaas heb je geen geld.")
        chapter_2_1()





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
                    player_moral += 5
                elif qp2 in no:
                    print("Je laat het liggen")

            else:
                print("Er is niks.")

        elif qp1 in move:
            print("Je pakt je rugzak op en vertrekt van de boot af.")
            wc1 = True
        
    time.sleep(5)

    print("Je loopt een pad samen met meerdere mensen. Na een tijdje ben je alleen in het bos.")

    time.sleep(5)

    wc2 = False
    while wc2 == False:
        qp3 = input("Wat wil je doen? ")
        if qp3 in look:
            print("Je ziet twee zand paden voor je. Achter je loopt een lang grind pad.")
            print("Terug in de verte zie je een stukje van het strand waar eerst de boot stond.")
            print("De bladeren van de bomen zijn olijf groen.")
            print("Je voelt een warme zomer bries.")
        elif qp3 in use:
            print("Op de grond liggen takjes en blaadjes, maar niks nuttigs.")
        elif qp3 in move:
            print("Je herrinert jezelf aan rechts aanhouden en kiest het rechter pad.")
            wc2 = True

    print("Je loopt en loopt. Na een tijdje kom je weer mensen tegen. Je herkent een aantal van de vluchtelingen.")
    print("Er lijkt iets aan de hand te zijn verderop.")

    time.sleep(10)

    wc3 = False
    while wc3 == False:
        qp4 = input("Wat wil je doen? ")
        if qp4 in look:
            print("Je staat op je tenen en ziet dat je bij een hek bent.")
            print("Je ziet dat er een ruzie is ontsaan tussen een vluchteling en een bewaker.")
            wc3 = True
        elif qp4 in use:
            print("Er is niks om te gebruiken.")
        elif qp4 in move:
            print("Er staan allemaal mensen dicht om je heen.")
            player_moral -= 1
    
    time.sleep(5)

    print("Bewaker: Hey! je moet op afstand blijven!")
    print("Vluchteling: Ik sta toch hier! En laat ons erdoor, we verhongeren hier!")

    time.sleep(2)

    print("De vluchteling duikt zijn zakken in. Je kunt zien dat hij zijn telefoon probeert te pakken,")
    print("maar de bewaker ziet dit niet en ziet het als een slecht teken.")
    print("De bewaker grijpt naar zijn wapen en schietr in de man zijn been.")
    print("De vluchteling schreeuwt het uit van de pijn en alle mensen om hem heen rennen weg of")
    print("proberen over het hek te klimmen. Het is chaos.")

    time.sleep(15)

    wc4 = False
    while wc4 == False:
        qp4 = input("Wat wil je doen? ")
        if qp4 in look:
            print("Je ziet allemaal mensen verschillende kanten opgaan.")
            print("Ook voel je een helse koppijn.")
            player_moral -= 1
        elif qp4 in use:
            print("Er is niks om te gebruiken.")
        elif qp4 in move:
            print("Je rent een stuk het bos in om een uitgang over het hek te zoeken.")
            print("Je vindt er een! je probeert er over te klimmen, maar ziet dan dat er prikkeldraad over heen zit.")
            print("Je doet je tas eroverheen en klimt eroverheen en pakt dan weer je tas op.")
            wc4 = True
    
    time.sleep(12)

    print("Je bent nu over het hek. je voelt je vermoeid maar probeert nog overeind te lopen.")
    print("Uiteindelijk kom je bij een treinspoor. Het is stil.")
    print("Door alle stress heb je geen honger. Je hoort de vogels fluiten en de bomen ritselen..")

    time.sleep(15)

    wc5 = False
    while wc5 == False:
        qp4 = input("Wat wil je doen? ")
        if qp4 in look:
            print("Je bent vermoeid.")
            print("Je loopt naast een treinspoor in een dal.")
        elif qp4 in use:
            print("Je hebt geen trek maar je denkt wel dat je honger hebt. Eten?")

            if "4 blikken voedsel" in inventory:
                qp2 = input()
                if qp2 in yes:
                    print("Je pakt je rugzak en haalt er twee blikken eten uit.")
                    print("Het is fruit en erwten.")
                    print("Je eet eerst het fruit en dan de erwten.")
                    print("De blikken zijn niet heel groot maar desondanks voel je je beter.")

                    inventory.append("2 blikken voedsel")
                    inventory.remove("4 blikken voedsel")
                    player_moral += 25
                elif qp2 in no:
                    print("Je besluit om niet te eten.")
            else:
                print("Je hebt geen eten.")

        elif qp4 in move:
            print("Je loopt verder langs het verlaten treinspoor.")
            wc5 = True
    
    time.sleep(5)

    print("Je loopt verder en verder. Na een tijdje is het laat in de avond.")
    print("Het begint zelfs nacht te worden.")
    print("Nog steeds voel je je vermoeid, maar al iets beter worden.")

    if "2 blikken voedsel" in inventory:
        print("Eten heeft erg geholpen!")

    time.sleep(10)

    print("na een tijdje vindt je een kist. hij zit volledig klem maar je denkt")
    print("als je een schroevendraaier hebt hem wel open kan krijgen.")

    if "Schroevendraaier" in inventory:
        qp5 = input("Wil je je schroevendraaier gebruiken? ")
        if qp5 in yes:
            print("Je vindt een zakmes en geld!")

            inventory.append("Zakmes")
            inventory.append("Geld")
            player_moral += 50
        elif qp5 in no:
            print("Je besluit om de kist niet open te maken.")
    else:
        print("Je hebt helaas geen schroevendraaier.")
    
    time.sleep(5)

    print("Je ziet uiteindelijk straat lichten in de verte.")
    print("Je begint uiteindelijk sneller lopen en komt dan in een dorp.")
    print("Het is nu nacht.")

    time.sleep(10)

    end_q = input("Wil je nu verder?:")
    if end_q in yes:
        os.system("cls")
        chapter_2()



        

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