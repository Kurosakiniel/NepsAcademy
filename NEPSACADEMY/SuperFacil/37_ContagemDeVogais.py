S = int(input())
N = input()

quantidadevogal = 0
for i in N:
    if i == "a":
        quantidadevogal += 1
    elif i == "e":
        quantidadevogal += 1
    elif i == "i":
        quantidadevogal += 1
    elif i == "o":
        quantidadevogal += 1
    elif i == "u":
        quantidadevogal += 1

print(quantidadevogal)