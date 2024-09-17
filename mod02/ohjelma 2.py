
nimi = input("Anna nimesi:")
# nimi = "Nari"
#\ on escape-merkki, jolla voi tuottaa tabin \t tai rivin \n
print("Hauska tavata," + nimi + "!")
ikä = input("Minkä ikäinen olet?")
#käyttäjän syöte on aina merkkijono
print("Ikäsi on\n" + ikä)
ikä =int(ikä) + 1
ikä_string = str(ikä)
print("Ikäsi on vuoden päästä\n" + str(ikä))
pituus = input("Minkä pituinen olet?")
print("olet\n" + pituus + "\npitkä")
print(f"Nimi: {nimi}, Ikä: {ikä-1}, Pituus: {pituus}")

