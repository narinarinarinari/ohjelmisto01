kala = float(input("Minkä pituisen kalan nappasit? (cm)"))
if kala > 37:
    print("Kalasi on tarpeeksi suuri, voit pitää sen.")
else:
    print("Kalasi on liian pieni, heitä se takaisin järveen!")
    print("Kalasi on", 37 - int(kala), "cm liian pieni.")
