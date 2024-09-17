#leiviskä 20 naulaa
#naula 32 luotia
#luoti 13,3g
import math
leiviskät = float(input("Anna leiviskät?"))
naulat = float(input("Anna naulat?"))
luodit = float(input("Anna luodit?"))
#selvitetään naulojen määrä
naulatTot = leiviskät * 20 + naulat
#luotien määrän selvittäminen
luoditTot = naulatTot * 32 + luodit

#lasketaan massa grammoina
grammaTot = luoditTot * 13.3
print (grammaTot)
kg = int(grammaTot/1000)
print ("Kokonais kg määrä", kg)
gr = grammaTot % 1000
print(f"Massa nykymittojen mukaan: {kg} kg ja {gr:.2f} grammaa")