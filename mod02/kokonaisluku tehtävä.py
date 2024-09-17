#kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon
import math
kl1 = str(input("Anna kokonaisluku"))
kl2 = str(input("Anna kokonaisluku"))
kl3 = str(input("Anna kokonaisluku"))
print("Valitsit kokonaisluvut" + kl1,kl2,kl3)
print("Lukujen summa on", int(kl1) + int(kl2) + int(kl3))
print("Lukujen tulo on", int(kl1) * int(kl2) * int(kl3))
print("Lukujen keskiarvo on", (int(kl1) + int(kl2) + int(kl3))/3)



