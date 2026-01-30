n = int(input())

somaUMMilhão = 0
contadorUmMilhao = 0

for i in range(n):
    a = int(input())
    somaUMMilhão += a
    i += 1
    if somaUMMilhão >= 1000000:
        if contadorUmMilhao == 0:
            contadorUmMilhao = i
        else:
            continue

print(contadorUmMilhao)