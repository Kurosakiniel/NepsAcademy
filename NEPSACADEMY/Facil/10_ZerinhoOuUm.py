A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)


if (A == B) and C != (A and B):
    print("C")
elif B == C and A != (B and C):
    print("A")
elif A == C and B != (A and C):
    print("B")
else:
    print("*")