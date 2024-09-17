import random
#π=4n/N
n = 0
N = 100
iterator = 0
while iterator < N:
    iterator += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä.")
komento = int(input("Anna pisteiden lukumäärä"))
while komento < N or komento > N:
    komento += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"Arvottu piste: {x}, {y}")
    print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä")
    else:
        print("Piste ei ole yksikköympyrässä")
