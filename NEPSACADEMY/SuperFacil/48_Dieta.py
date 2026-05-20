n, m = input().split()

n = int(n)
m = int(m)

quantidadeProteina = 0
quantidadeGordura = 0
quantidadeCarboidrato = 0

for i in range(n):
    p, g, c = input().split()

    p = int(p)
    g = int(g)
    c = int(c)
    
    quantidadeProteina += p

    quantidadeGordura += g

    quantidadeCarboidrato += c


somaTotal = ((quantidadeProteina * 4) + (quantidadeGordura * 9) + (quantidadeCarboidrato * 4))
totalCarboidrado = (m - somaTotal)

if totalCarboidrado <= - 0:
    print("0")
else:
    print(totalCarboidrado)
