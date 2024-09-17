def is_prime_number(num):
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)
        if num % i == 0:
         return False
    return True

user_input = int(input("Anna testattava kokonaisluku (>0):"))
if is_prime_number(user_input):
    print(f"{user_input} on alkuluku")
else:
    print(f"{user_input} ei ole alkuluku")