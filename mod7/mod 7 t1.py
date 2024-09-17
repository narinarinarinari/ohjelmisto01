vuodenajat = "kevät", "kesä", "syksy", "talvi"
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12), niin kerron vuodenajan:"))
if järjestysnumero >= 3 and järjestysnumero <= 5:
    print("Vuodenaika on kevät!")
elif järjestysnumero >= 6 and järjestysnumero <= 8:
    print("Vuodenaika on kesä!")
elif järjestysnumero >= 9 and järjestysnumero <= 11:
    print("Vuodenaika on syksy!")
elif järjestysnumero == 12 or järjestysnumero >=1 and järjestysnumero <=2:
    print("Vuodenaika on talvi!")
else:
    print("Virheellinen järjestysnumero.")