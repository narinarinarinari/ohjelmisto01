hytti = str(input("Mikä on hyttiluokkasi? Valitse A, B C tai LUX."))
if hytti == "A":
    print("Hyttisi on ikkunallinen hytti autokannen yläpuolella.")
elif hytti == "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella.")
elif hytti == "B" or hytti == "C":
    print("Hyttisi on ikkunaton hytti autokannen yläpuolella")
else:
    print("Virheellinen hyttiluokka")
