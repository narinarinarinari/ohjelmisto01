nums = []

num = input("Anna ensimmäinen luku tai lopeta painamalla ENTER: ")
while num !="":
    nums.append(num)
    num = input("Anna lisää lukuja tai lopeta painamalla ENTER: ")

print(nums)

nums.sort(reverse=True)
print(nums)
