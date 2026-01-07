P, R = input().split()

P = int(P)
R = int(R)

if P == 1 and R == 0:
    print("B")
elif P == 1 and R == 1:
    print("A")
else:
    print("C")