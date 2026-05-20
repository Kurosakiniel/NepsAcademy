N = int(input())

n = str(N)
numeros = list(n)
decimal = numeros[0]
unidade = numeros[1]

if decimal == unidade:
    print("1")
else:
    print("0")