x = int(input())

for i in range(1,x + 1):
    if x % i == 0:
        print(i, end= " ")
        i += 1
    else: 
        i += 1

"""

Fiz essa buceta 3 vezes pq tava dando

"""

"""
x = int(input())

for i in range(1,x + 1):
    divisao = x // i
    if (x // i % 2 == 0) or (i * 1 == x) or (x * i == x):
        print(i, end = " ")
        i += 1
    elif (divisao * 2 == x) or (divisao * i == x):
        print(i, end = " ")
        i += 1
    else:
        i += 1
"""

"""

count = 1
while count <= x:
    divisao = x // count
    if x / count % 2 == 0:
        print(count, end=" ")
        count += 1
    elif count * 1 == x:
        print(count, end = " ")
        count += 1
    elif x * count == x:
        print(count, end = " ")
        count += 1
    elif divisao * 2 == x:
        print(count, end = " ")
        count += 1
    elif divisao * count == x:
        print(count, end = " ")
        count += 1
    else:
        count += 1

"""