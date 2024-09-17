import math
hg = int(input("Anna hemoglobiiniarvosi (g/l):"))
sp = str(input("Anna sukupuolesi (mies/nainen):"))

if sp == "nainen" and 175 >= hg >= 117:
    print("Hemoglobiiniarvosi on normaali")
elif sp == "nainen" and hg > 175:
    print("Hemoglobiiniarvosi on korkea")
elif sp == "nainen" and hg < 117:
    print("Hemoglobiiniarvosi on matala")

if sp == "mies" and 195 >= hg >= 134:
    print("Hemoglobiiniarvosi on normaali")
elif sp == "mies" and hg > 195:
    print("Hemoglobiiniarvosi on korkea")
elif sp== "mies" and hg < 134:
    print("Hemoglobiiniarvosi on matala")
