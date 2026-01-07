s = input()
c = input()
count = 0
letrasIguais = 0

for i in list(s):
    if c == i:
        letrasIguais += 1

print(letrasIguais)