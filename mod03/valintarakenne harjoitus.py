# if-ehto, "jos a, niin b" Alustus ehtolauseelle:
rahat = float(input("Paljonko sinulla on rahaa?"))
#bolean on muuttuja, joka on true tai false
ehto = (rahat >=5)
print(ehto)
if ehto:
    print("Voit ostaa latten.")
else:
    print("Olet liian köyhä ostamaan latten. Mene töihin!")

#toinen ohjelma koska tämä on hiekkalaatikko lol

suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")
else:
    print("Juuh ei ne ollukkaa kaimoja.")

#kolmas harjotus

luku = int(input("Anna luku?"))
if luku>0:
    print("Numero on positiivinen")
if luku<0:
    print("Numero on negatiivinen")
if luku==0:
    print("Numero on 0")

#Nyt käytetään edellistä rakennetta pienellä twistillä

Ikä = int(input("Anna ikäsi:"))
if Ikä>=65:
    print("Olet eläkeikäinen.")
elif Ikä>=18:
    print("Olet työiässä.")
elif Ikä>=7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")

#jotain

user_input = input("Valitse a, b tai c")
if user_input=="a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input=="b":
    print("Tehdään jotain muuta kivaa, käyttäjä valitsi kirjaimen b")
#lohkossa on usein paljonkin koodia ja kaikki sisennetty suoritetaan, mikäli ehdot täyttyy
elif user_input=="c":
    print("Käyttäjä valitsi c")
    print("Moikka saat rahaa 1000 lanttia")
else:
    print("Opettele kirjoittamaan! Pyysin sinua kirjoittamaan a, b tai c. Emme tee nyt mitään.")
print("Ohjelma loppuu, heihei!")