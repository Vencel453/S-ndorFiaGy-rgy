import math

a = int(input("1. oldal: "))
b = int(input("2. oldal: "))
c = int(input("3. oldal: "))

if a > b and a > c:
    átfogó = a
    befogó1 = b
    befogó2 = c
elif b > a and b > c:
    átfogó = b
    befogó1 = a
    befogó2 = c
else:
    átfogó = c
    befogó1 = a
    befogó2 = b

if math.pow(befogó1, 2) + math.pow(befogó2, 2) == math.pow(átfogó, 2):
    print("Derékszögű háromszög")
else:
    print("Nem derékszögű háromszög")