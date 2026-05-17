# um numero que determina a quantadde de vezes q vai ser imprimido
# duas entradas ( em split ) um pra um numero e um pra um simbolo
# a saida deve ser a qunatidade de simbolos baseada no numero e a quantidade determinada no primeiro

# logica
# ter um numero de entrada
# esse numero de entrada vai ser o contador do while
# dentro do while vai ter o split
# vai converter a quantidade de vezes que vai aparecer o simbolo ( usando for )
# vai printar  printar essa quantidade.

l = int(input())

for i in range(l):
    a, b = input().split()

    a = int(a)
    b = str(b)

for i in range(a):
    print(b, end="")
