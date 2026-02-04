s = int(input())
m = int(input())
l = int(input())

indiceDeFelicidade = (1 * s + 2 * m + 3 * l)

if indiceDeFelicidade >= 10:
    print("happy")
else:
    print("sad")