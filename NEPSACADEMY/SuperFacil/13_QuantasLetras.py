s = input()
c = input()
letrasIguais = 0

for i in list(s):
    if c == i:
        letrasIguais += 1

print(letrasIguais)