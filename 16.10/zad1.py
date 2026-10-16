n = int (input("Брой числа: "))
x = int (input("Въведи първото число: "))
maxn= x
for i in range (n-1):
    x= int (input("Въведи число: "))

    if x > maxn:
        maxn = x

print("Най-голямото число е : ", maxn)
