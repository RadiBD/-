
a = int(input("Въведи долната граница: "))
b = int(input("Въведи горната граница: "))

broi = 0

for i in range(10):
    n = int(input("Въведи число: "))

    if n >= a and n <= b:
        broi = broi + 1

print("Броят на числата в интервала е:", broi)
