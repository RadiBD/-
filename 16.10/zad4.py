
n = int(input("Въведи число: "))

if n < 2:
    print("Числото не е просто")
else:
    prosto = True

    for i in range(2, n):
        if n % i == 0:
            prosto = False

    if prosto == True:
        print("Числото е просто")
    else:
        print("Числото не е просто")
