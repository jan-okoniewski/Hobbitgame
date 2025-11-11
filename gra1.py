### Template of a room
def pok_1():
    print("Opis miejsca gdzie jesteś")
    print("Wyjścia: N O S W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        koniecb()
    elif (direction=="O"):
        koniecb()
    elif (direction=="S"):
        koniecb()
    elif (direction == "W"):
        koniecb()
    else:
        print("Nie rozumię")
        pok_1()

def koniecb():
    print("Wpadles do zapadni i nie morzesz wyjść to koniec!")

def pok_start():
    print("Jesteś przed norką hobbita. Na N są okrągłe drzwi, na O/S/W jest pole")
    print("Wyjścia: N")
    direction = input("Co robisz? ")
    if (direction=="N"):
        pok_sien()
    else:
        print("Nie rozumię")
        pok_start()

def pok_sien():
    print("Jesteś w sieni norki hobbita. Na S są okrągłe drzwi, na N są drzwi dalej do norki")
    print("Wyjścia: N S")
    direction = input("Co robisz? ")
    if (direction=="N"):
        salon_1()
    elif (direction=="S"):
        pok_start()
    else:
        print("Nie rozumię")
        pok_sien()


def salon_1():
    print("Jestes w salonie, spotykasz bilbo mówi ci rze ma w domu skarb i muśsz go znalezici")
    print("Wyjścia: N O S W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        korytaż_1()
    elif (direction=="O"):
        kuchnia()
    elif (direction=="S"):
        pok_sien()
    elif (direction == "W"):
        sypialnia()
    else:
        print("Nie rozumię")
        salon_1()


def sypialnia():
    print("jesteś jesteś w sypialni jest pokój zamknienty na klucz naszczęśće lerzy na bardrzo wysokiej szafie ale dośęgeśz")
    print("Wyjścia: N O")
    direction = input("Co robisz? ")
    if (direction == "N"):
        komura()
    elif (direction == "O"):
        salon_1()
    else:
        print("Nie rozumię")
        sypialnia()


def kuchnia():
    print("jesteś w kuchni wiśi tu durzo kiełbas cebuli i czosnku")
    print("Wyjścia: O S W")
    direction = input("Co robisz? ")
    if (direction == "O"):
        biuro()
    elif (direction == "S"):
        spirzarnia()
    elif (direction == "W"):
        salon_1()
    else:
        print("Nie rozumię")
        kuchnia()



def korytaż_1():
    print("jesteś w korytarzu")
    print("Wyjścia: N S")
    direction = input("Co robisz? ")
    if (direction=="N"):
        wc1()
    elif (direction=="S"):
        salon_1()
    else:
        print("Nie rozumię")
        korytaż_1()


def spirzarnia():
    print("jesteś w spirzarni ")
    print("Wyjścia: N O")
    direction = input("Co robisz? ")
    if (direction=="N"):
        kuchnia()
    elif (direction=="O"):
        salon2()
    else:
        print("Nie rozumię")
        spirzarnia()

def biuro():
    print("jesteś w biurze")
    print("Wyjścia: N O S W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        koniecb() #wc2
    elif (direction=="O"):
        wendzarnia,piekarnia()
    elif (direction=="S"):
        salon2()
    elif (direction == "W"):
        kuchnia()
    else:
        print("Nie rozumię")
        biuro()


def komura():
    print("jesteś w małym zakurzonym pokojiku")
    print("Wyjścia: N S W")
    direction = input("Co robisz? ")
    if (direction == "N"):
        pokujobrazowy()
    elif (direction == "S"):
        sypialnia()
    elif (direction == "W"):
        zbrojnia()
    else:
        print("Nie rozumię")
        komura()


def salon2():
    print("jesteś w salonie 2 spsząta tam spszątaczka")
    print("Wyjścia: N O W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        biuro()
    elif (direction=="O"):
        drewnonaopal()
    elif (direction == "W"):
        spirzarnia()
    else:
        print("Nie rozumię")
        salon2()

def wc1():
    print("jesteś teraz w głuwnym WC")
    print("Wyjścia: N O S W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        szafyzubranianiami()
    elif (direction=="O"):
        sauna()
    elif (direction=="S"):
        korytaż_1()
    elif (direction == "W"):
        pokujobrazowy()
    else:
        print("Nie rozumię")
        wc1()

def pokujobrazowy():
    print("jesteś w pokoju pełnym obrazów")
    print("Wyjścia: N O")
    direction = input("Co robisz? ")
    if (direction=="N"):
        trofea()
    elif (direction=="O"):
        wc1()
    else:
        print("Nie rozumię")
        pokujobrazowy()

def zbrojnia():
    print("jesteś w pokoju pełnym broni")
    print("Wyjścia: N O W")
    direction = input("Co robisz? ")
    if (direction=="N"):
        zakok()
    elif (direction=="O"):
        komura()
    elif (direction == "W"):
        zapad()
    else:
        print("Nie rozumię")
        zbrojnia()


def zapad():
    print("Zapadnia")
    print("Wyjścia: nie ma kliknij N")
    direction = input("Co robisz? ")
    if (direction=="N"):
        koniecb()
        print("Nie rozumię")
        zapad()


def zakok():
    print("jesteś w ciemnym pokojó som hiroglify o skarbie")
    print("Wyjścia: S W ")
    direction = input("Co robisz? ")
    if (direction=="S"):
        zbrojnia()
    elif (direction == "W"):
        Skarb()
    else:
        print("Nie rozumię")
        zakok()


def Skarb():
    print("koniec jest skarb jak n to restart")
    print("Wyjścia:N ")
    direction = input("Co robisz? ")
    if (direction=="N"):
        pok_start()
    else:
        print("Nie rozumię")
        Skarb()



def trofea():
    print("Opis miejsca gdzie jesteś")
    print("Wyjścia: S")
    direction = input("Co robisz? ")
    if (direction=="S"):
        pokujobrazowy()
    else:
        print("Nie rozumię")
        trofea()


def drewnonaopal():
    print("Opis miejsca gdzie jesteś")
    print("Wyjścia: W")
    direction = input("Co robisz? ")
    if (direction == "W"):
        salon2()
    else:
        print("Nie rozumię")
        pok_1()
## Uruchomienie
pok_start()




