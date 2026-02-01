n = int(input())
quantidadeDeCoposQuebrados = 0

for i in range(n):
    l, c = input().split()
    l = int(l)
    c = int(c)

    if l > c:
        quantidadeDeCoposQuebrados += c
    else:
        i += 1

print(quantidadeDeCoposQuebrados)