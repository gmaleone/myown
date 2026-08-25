# ===== WHILE LOOP =====

count = 1

while count <= 5:
    print(count)
    count = count + 1


print("---")

count = 1

while count <= 10:
    print(count)
    count = count + 1

print("Sickk!")


print("---")


numbers = [5,10,15,20]
total = 0
i = 0

while i < len(numbers):
    total = total + numbers[i]
    i = i + 1
print("Total",total)