import random
total = 0
results = []
dice_count= int(input("Montako noppaa arvotaan?"))
for i in range(dice_count):
    result = random.randint(1,6)
    total = total + result
    results.append(result)
print(f"Noppien silmälukujen summa on: {sum(results)}, nopat: {results}")


