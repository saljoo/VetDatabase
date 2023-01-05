#Funktio uuden potilaan lisäämiseksi
def uuden_potilaan_lisays(asiakasnumero: int, nimi: str, laji: str, syntymaaika: str, kaynninSyy: str):
    #Avataan tietokanta kirjoitusmuodossa
    laakarinTietokanta = open("elainlaakarin_tietokanta.txt", "a")
    #Lisätään tietokantaan uusi potilas
    laakarinTietokanta.write(f"Asiakasnumero: {asiakasnumero}, Nimi: {nimi}, Laji: {laji}, Syntymäaika: {syntymaaika}, Käynnin syy: {kaynninSyy}\n")
    laakarinTietokanta.close()

#Funktio potilaan poistamiseksi tietokannasta
def potilaan_poisto(asiakasnumero: int):
    #Tyhjä lista, johon tallennetaan potilaat tietokannasta
    listaPotilaista = []
    #Avataan tietokanta lukumuodossa ja luetaan jokainen rivi listan alkioiksi
    laakarinTietokanta = open("elainlaakarin_tietokanta.txt", "r")
    listaPotilaista = laakarinTietokanta.readlines()
    
    #Avataan tietokanta kirjoitusmuodossa
    laakarinTietokanta = open("elainlaakarin_tietokanta.txt", "w")
    #Ylikirjoitetaan tietokanta niin, että tietokantaan kirjoitetaan uudestaan kaikki muut potilaat
    #paitsi potilas, joka halutaan poistaa
    for rivi in listaPotilaista:
        if str(asiakasnumero) not in rivi:
            laakarinTietokanta.write(rivi)
    laakarinTietokanta.close()

#Funktio potilaan hakuun
def potilaan_haku(hakuTermi, valinta):
    #Tyhjä lista, johon tallennetaan potilaat tietokannasta
    listaPotilaista = []
    #Avataan tietokanta lukumuodossa ja luetaan jokainen rivi listan alkioiksi
    laakarinTietokanta = open("elainlaakarin_tietokanta.txt", "r")
    listaPotilaista = laakarinTietokanta.readlines()
    laakarinTietokanta.close()
    listaPotilaista.sort()
    loytyi = False

    #Haku asiakasnumerolla
    if valinta == 1:
        if hakuTermi == "kaikki":
            for rivi in listaPotilaista:
                rivi = rivi.strip()
                if len(rivi) > 1:
                    print(rivi)
        else:
            for rivi in listaPotilaista:
                rivi = rivi.strip()
                if hakuTermi in rivi[rivi.find("Asiakasnumero:"):rivi.find("Nimi:")]:
                    print(rivi)
                    loytyi = True
            if loytyi == False:
                print("Yhtään potilasta ei löytynyt kyseisellä asiakasnumerolla.")
    #Haku nimellä
    elif valinta == 2:
        for rivi in listaPotilaista:
            rivi = rivi.strip()
            if hakuTermi in rivi[rivi.find("Nimi:"):rivi.find("Laji:")]:
                print(rivi)
                loytyi = True
        if loytyi == False:
            print("Yhtään potilasta ei löytynyt kyseisellä nimellä.")
    #Haku lajin perusteella
    elif valinta == 3:
        for rivi in listaPotilaista:
            rivi = rivi.strip()
            if hakuTermi in rivi[rivi.find("Laji:"):rivi.find("Syntymäaika:")]:
                print(rivi)
                loytyi = True
        if loytyi == False:
            print("Yhtään potilasta ei löytynyt kyseisellä lajilla.")
    #Haku syntymäajan perusteella
    elif valinta == 4:
        for rivi in listaPotilaista:
            rivi = rivi.strip()
            if hakuTermi in rivi[rivi.find("Syntymäaika:"):rivi.find("Käynnin syy:")]:
                print(rivi)
                loytyi = True
        if loytyi == False:
            print("Yhtään potilasta ei löytynyt kyseisellä syntymäajalla.")
    #Haku käynnin syyn perusteella
    elif valinta == 5:
        for rivi in listaPotilaista:
            rivi = rivi.strip()
            if hakuTermi in rivi[rivi.find("Käynnin syy:"):]:
                print(rivi)
                loytyi = True
        if loytyi == False:
            print("Yhtään potilasta ei löytynyt kyseisellä käynnin syyllä.")
       


#Pääohjelma joka on käynnissä kunnes käyttäjä lopettaa valitsemalla nollan
while True:
    #Tulostetaan tietokannan käyttövaihtoehdot
    print("Poistu: 0")
    print("Potilaan lisäys: 1")
    print("Potilaiden haku: 2")
    print("Potilaan poisto: 3")
    #Kysytään käyttäjän valinta
    valinta = int(input("Valinta: "))
    print("")

    #Lopetetaan ohjelma
    if valinta == 0:
        break

    #Lisätään uusi potilas tietokantaan
    elif valinta == 1:
        asiakasnumero = int(input("Asiakasnumero: "))
        nimi = input("Nimi: ")
        laji = input("Laji: ")
        syntymaaika = input("Syntymäaika: ")
        kaynninSyy = input("Käynnin syy: ")
        uuden_potilaan_lisays(asiakasnumero, nimi, laji, syntymaaika, kaynninSyy)
        print("Potilaan lisäys onnistui.\n")

    #Haetaan tietokannasta potilaita eri kriteereillä
    elif valinta == 2:
        print("Haku asiakasnumerolla: 1")
        print("Haku nimellä: 2")
        print("Haku lajin perusteella: 3")
        print("Haku syntymäajalla: 4")
        print("Haku käynnin syyn perusteella: 5")
        uusiValinta = int(input("Valinta: "))

        if uusiValinta == 1:
            asiakasnumero = str(input("Asiakasnumero: "))
            potilaan_haku(asiakasnumero, uusiValinta)
        elif uusiValinta == 2:
            nimi = input("Nimi: ")
            potilaan_haku(nimi, uusiValinta)
        elif uusiValinta == 3:
            laji = input("Laji: ")
            potilaan_haku(laji, uusiValinta)
        elif uusiValinta == 4:
            syntymaaika = input("Syntymäaika: ")
            potilaan_haku(syntymaaika, uusiValinta)
        elif uusiValinta == 5:
            kaynninSyy = input("Käynnin syy: ")
            potilaan_haku(kaynninSyy, uusiValinta)

    #Poistetaan potilas tietokannasta
    elif valinta == 3:
        asiakasnumero = int(input("Asiakasnumero: "))
        potilaan_poisto(asiakasnumero)
        print("Potilaan poistaminen onnistui.\n")