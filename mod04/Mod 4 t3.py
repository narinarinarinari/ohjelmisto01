max_num = -100
min_num = 100
input_string = input("Syötä luku: ")
if input_string != "":
    max_num = min_num = int(input_string)
while input_string != "":
    input_string = (input("Syötä luku: "))
    if input_string != "":
     number = int(input("Syötä luku: "))
     if number > max_num:
        max_num = number
     if number < min_num:
        min_num = number
     print(f"Pienin numero: {min_num}, suurin numero: {max_num}")



